"""
rag.py
Core RAG logic — ties everything together.

This file has two main jobs:
1. index_contract()  — called when a contract is uploaded or saved
2. query_contract()  — called when user asks a question in AI Copilot
"""

import httpx
import re
from app.config import OLLAMA_BASE_URL, OLLAMA_CHAT_MODEL
from app.services.chunker import chunk_text
from app.services.embeddings import get_embedding, get_embeddings_batch
from app.services.vectorstore import save_chunks, search_similar_chunks, get_contract_chunks


# ─── INDEXING ────────────────────────────────────────────────────────────────

async def index_contract(contract_id: str, text: str, title: str = "") -> int:
    """
    Index a contract for RAG.

    Steps:
    1. Split the contract text into chunks
    2. Generate an embedding for each chunk
    3. Save chunks + embeddings to ChromaDB
    """
    chunks = chunk_text(text, chunk_size=500, overlap=100)

    if not chunks:
        return 0

    chunk_texts = [c["text"] for c in chunks]
    embeddings = await get_embeddings_batch(chunk_texts)

    save_chunks(contract_id, chunks, embeddings)
    return len(chunks)


# ─── QUERYING ─────────────────────────────────────────────────────────────────

ANALYSIS_KEYWORDS = {
    "analyze", "analysis", "summary", "summarize", "overview", "review",
    "audit", "breakdown", "explain", "risks", "risk", "clauses", "tell me about",
    "what is this contract", "what does this contract", "contract details"
}


def _is_analysis_query(question: str) -> bool:
    """Check if the user is asking for a general/holistic contract analysis or review."""
    q_lower = question.lower().strip()
    return any(kw in q_lower for kw in ANALYSIS_KEYWORDS)


def _is_pure_greeting(question: str) -> bool:
    """Check if the message is strictly a greeting without any command."""
    q_clean = re.sub(r"[^a-zA-Z\s]", "", question.lower()).strip()
    return q_clean in {"hi", "hello", "hey", "good morning", "good evening", "greetings"}


async def query_contract(contract_id: str, question: str) -> dict:
    """
    Answer a user's prompt using Lexora Origin v1 RAG intelligence.

    Handles:
    - Holistic Contract Analysis ("analyze this contract", "summarize risks")
    - Specific Clause / Factual Q&A ("what are the payment terms?")
    - Legal Clause Drafting ("draft a mutual indemnification clause")
    - General Inquiries & Greetings
    """
    is_analysis = _is_analysis_query(question)
    is_greeting = _is_pure_greeting(question)

    # 1. Pure Greeting Handler
    if is_greeting:
        return {
            "answer": (
                "Hello! I am **Lexora Origin v1**, your AI Legal Copilot. ⚖️\n\n"
                "I have analyzed this contract and am ready to assist you. You can ask me to:\n"
                "• **Analyze or summarize** the entire agreement\n"
                "• **Check specific terms** (penalties, payment, notice periods, jurisdiction)\n"
                "• **Identify risks** (liability caps, indemnification, termination traps)\n"
                "• **Draft or refine clauses** to protect your interests\n\n"
                "How can I help you with this document today?"
            ),
            "sources": [],
        }

    # 2. Retrieve Chunks
    # For comprehensive analysis, fetch sequential document chunks (up to 12)
    if is_analysis:
        doc_data = get_contract_chunks(contract_id, limit=12)
        all_chunks = doc_data.get("chunks", [])
        
        if all_chunks:
            # Sort chronologically by chunk_index
            all_chunks = sorted(all_chunks, key=lambda x: x.get("chunk_index", 0))
            relevant_chunks = [
                {"text": c["text"], "chunk_index": c.get("chunk_index", idx)}
                for idx, c in enumerate(all_chunks)
            ]
        else:
            # Fallback to vector search if no direct collection
            query_embedding = await get_embedding(question)
            relevant_chunks = search_similar_chunks(contract_id, query_embedding, top_k=8)
    else:
        # Factual or specific question -> targeted vector search
        query_embedding = await get_embedding(question)
        relevant_chunks = search_similar_chunks(contract_id, query_embedding, top_k=6)

    # If no chunks at all
    if not relevant_chunks:
        context = "No contract text found in database."
    else:
        context = "\n\n---\n\n".join(
            [f"[Excerpt {i+1} - Chunk {chunk['chunk_index']}]:\n{chunk['text']}" 
             for i, chunk in enumerate(relevant_chunks)]
        )

    # 3. Build Prompt Based on Query Type
    if is_analysis:
        prompt = f"""You are Lexora Origin v1, an elite legal intelligence model and contract analysis copilot.
Perform a thorough, executive-level LEGAL ANALYSIS of the contract based on the excerpts provided below.

CONTRACT CONTEXT:
\"\"\"
{context}
\"\"\"

USER REQUEST:
\"{question}\"

Provide a structured, professional legal analysis using this clear format:

### 📋 1. Executive Summary & Purpose
Provide a concise overview of what this agreement governs and its primary intent.

### 👥 2. Key Parties & Duration
Identify the contracting parties, effective date, and term length.

### 💰 3. Financial & Payment Terms
Detail the payment amounts, due dates, and any late payment fees or penalties.

### ⚠️ 4. Key Risk Assessment & Red Flags
Highlight critical liability, indemnification, termination rules, and potential exposure areas.

### ⚖️ 5. Governing Law & Dispute Resolution
State the applicable jurisdiction and arbitration/court mechanism.

### 💡 6. Strategic Legal Recommendations
Provide 2-3 practical recommendations to improve or protect the client's interests.

ANALYSIS:"""

    else:
        prompt = f"""You are Lexora Origin v1, an elite AI legal copilot for contract review and drafting.

CONTRACT CONTEXT:
\"\"\"
{context}
\"\"\"

USER REQUEST / QUESTION:
\"{question}\"

INSTRUCTIONS:
1. If the user asks about factual terms in this contract (e.g. payment terms, penalties, termination notice, indemnity, parties):
   - Answer accurately based on the excerpts.
   - Quote exact figures, timelines, and clause names where applicable.
2. If the user asks you to draft or modify a legal clause (e.g. "Draft an NDA clause", "Add a non-compete clause"):
   - Draft a complete, professional, attorney-grade legal clause tailored to the contract context.
3. If a factual term is genuinely absent from the excerpts:
   - State clearly that the term is not specified in the provided contract excerpts, and provide a recommended standard clause.

ANSWER:"""

    # 4. Generate Response via Ollama
    answer = await _call_ollama_chat(prompt)

    return {
        "answer": answer,
        "sources": [
            {"text": c["text"], "chunk_index": c["chunk_index"]}
            for c in relevant_chunks
        ] if relevant_chunks else [],
    }


# ─── HELPER: Call Ollama Chat ─────────────────────────────────────────────────

async def _call_ollama_chat(prompt: str) -> str:
    """
    Send prompt to Ollama model.
    """
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_CHAT_MODEL,
                "prompt": prompt,
                "stream": False,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["response"].strip()
