"""
rag.py
Core RAG logic — Indian Legal Framework Edition with Pre-Indexed Statutory Knowledge Base.

Specialized for Indian Contract Law:
- The Indian Contract Act, 1872
- The Arbitration and Conciliation Act, 1996
- The Indian Stamp Act, 1899 & Registration Act, 1908
- The MSMED Act, 2006 (MSME 45-day payment rules)
- The Digital Personal Data Protection (DPDP) Act, 2023 & IT Act, 2000
"""

import httpx
import json
import re
from typing import AsyncGenerator
from app.config import OLLAMA_BASE_URL, OLLAMA_CHAT_MODEL
from app.services.chunker import chunk_text
from app.services.embeddings import get_embedding, get_embeddings_batch
from app.services.vectorstore import save_chunks, search_similar_chunks, get_contract_chunks
from app.services.seed_indian_law import search_indian_law_statutes


# ─── INDEXING ────────────────────────────────────────────────────────────────

async def index_contract(contract_id: str, text: str, title: str = "") -> int:
    """
    Index a contract for RAG.
    """
    chunks = chunk_text(text, chunk_size=500, overlap=100)

    if not chunks:
        return 0

    chunk_texts = [c["text"] for c in chunks]
    embeddings = await get_embeddings_batch(chunk_texts)

    save_chunks(contract_id, chunks, embeddings)
    return len(chunks)


# ─── INTENT CLASSIFIERS ───────────────────────────────────────────────────────

ANALYSIS_KEYWORDS = {
    "analyze", "analysis", "summary", "summarize", "overview", "review",
    "audit", "breakdown", "explain", "risks", "risk", "clauses", "tell me about",
    "what is this contract", "what does this contract", "contract details",
    "compliance", "stamp duty", "indian law", "arbitration", "research"
}


def _is_analysis_query(question: str) -> bool:
    """Check if the user is asking for a holistic contract analysis or legal audit."""
    q_lower = question.lower().strip()
    return any(kw in q_lower for kw in ANALYSIS_KEYWORDS)


def _is_pure_greeting(question: str) -> bool:
    """Check if the message is strictly a greeting."""
    q_clean = re.sub(r"[^a-zA-Z\s]", "", question.lower()).strip()
    return q_clean in {"hi", "hello", "hey", "good morning", "good evening", "greetings", "namaste"}


# ─── PROMPT & CONTEXT BUILDER ─────────────────────────────────────────────────

async def _build_rag_context_and_prompt(contract_id: str, question: str):
    """
    Retrieves contract chunks + Indian statutory law chunks from ChromaDB.
    """
    is_analysis = _is_analysis_query(question)
    is_greeting = _is_pure_greeting(question)

    if is_greeting:
        greeting_text = (
            "Namaste! I am **Lexora Origin v1 (India Edition)**, your AI Indian Legal Copilot. ⚖️🇮🇳\n\n"
            "I specialize in Indian contract law, statutory compliance, and legal research. You can ask me to:\n"
            "• **Audit & Analyze** this agreement under the **Indian Contract Act, 1872**\n"
            "• **Perform Legal Research** on Indian statutes (Section 27 non-compete, MSME 45-day rules, Stamp Duty)\n"
            "• **Verify terms & penalties** (Consideration in ₹, interest rates, notice periods)\n"
            "• **Review Arbitration & Jurisdiction** (Seat vs. Venue under Arbitration & Conciliation Act, 1996)\n"
            "• **Draft court-tested legal clauses** tailored to Indian High Courts & Supreme Court\n\n"
            "How can I assist you today?"
        )
        return None, [], True, greeting_text

    # 1. Retrieve Contract Chunks
    query_embedding = await get_embedding(question)

    if is_analysis:
        doc_data = get_contract_chunks(contract_id, limit=12)
        all_chunks = doc_data.get("chunks", [])
        
        if all_chunks:
            all_chunks = sorted(all_chunks, key=lambda x: x.get("chunk_index", 0))
            contract_chunks = [
                {"text": c["text"], "chunk_index": c.get("chunk_index", idx)}
                for idx, c in enumerate(all_chunks)
            ]
        else:
            contract_chunks = search_similar_chunks(contract_id, query_embedding, top_k=8)
    else:
        contract_chunks = search_similar_chunks(contract_id, query_embedding, top_k=6)

    # 2. Retrieve Relevant Indian Statutory Chunks from ChromaDB
    statute_chunks = search_indian_law_statutes(query_embedding, top_k=3)

    # Format Contract Context
    if not contract_chunks:
        contract_context = "No specific contract excerpts found."
    else:
        contract_context = "\n\n---\n\n".join(
            [f"[Contract Excerpt {i+1} - Chunk {chunk['chunk_index']}]:\n{chunk['text']}" 
             for i, chunk in enumerate(contract_chunks)]
        )

    # Format Statute Context
    if not statute_chunks:
        statute_context = "General Indian Contract Law Principles apply."
    else:
        statute_context = "\n\n---\n\n".join(
            [f"[Indian Statute Authority - {s.get('section', '')}]:\n{s.get('text', '')}" 
             for s in statute_chunks]
        )

    # 3. Build Prompt Based on Indian Legal Framework
    if is_analysis:
        prompt = f"""You are Lexora Origin v1 (India Edition), an elite Indian Legal Intelligence Engine and expert counsel.
Perform an executive-level LEGAL ANALYSIS of this agreement under the Indian Legal Framework (Indian Contract Act 1872, Arbitration & Conciliation Act 1996, MSMED Act 2006, Stamp Act, DPDP Act 2023).

RELEVANT INDIAN STATUTORY LAW & PRECEDENTS (FROM CHROMADB KNOWLEDGE BASE):
\"\"\"
{statute_context}
\"\"\"

CONTRACT EXCERPTS:
\"\"\"
{contract_context}
\"\"\"

USER REQUEST:
\"{question}\"

Provide a structured, partner-grade Indian legal analysis in this exact format:

### 📋 1. Executive Summary & Nature of Agreement
Define the legal nature of this contract under Indian law (e.g. Leave & License, Commercial Lease, MSA, Service Contract) and its primary commercial intent.

### 👥 2. Contracting Parties & Term
List the parties, execution date, effective date, and tenure of the agreement.

### 💰 3. Consideration & Financial Terms
Detail the payment consideration (in INR ₹ where applicable), payment schedules, GST/TDS provisions, and late payment interest or penalties.

### ⚠️ 4. Key Risk Assessment & Statutory Red Flags
Highlight critical liability exposures under Indian Law:
- Enforceability under Section 27 of Indian Contract Act (e.g., non-compete restrictions)
- Liquidated damages vs. Penalty under Section 74 of Indian Contract Act
- Indemnity and limitation of liability exposures
- Termination lock-in periods or notice traps

### ⚖️ 5. Governing Law, Dispute Resolution & Arbitration
Examine the dispute resolution mechanism (Arbitration under the Arbitration & Conciliation Act, 1996, Seat vs. Venue, and exclusive jurisdiction of Indian courts).

### 📜 6. Stamp Duty & Enforceability Advisory
Provide practical guidance on required Stamp Duty under applicable State Stamp Laws (e.g., Maharashtra/Karnataka/Delhi Stamp Act) and registration requirements under the Registration Act, 1908.

### 💡 7. Strategic Legal Recommendations
Provide 2-3 actionable, high-impact suggestions to safeguard the client's interests.

INDIAN LEGAL ANALYSIS:"""

    else:
        prompt = f"""You are Lexora Origin v1 (India Edition), an elite Indian legal AI copilot.

RELEVANT INDIAN STATUTORY LAW & PRECEDENTS (FROM CHROMADB KNOWLEDGE BASE):
\"\"\"
{statute_context}
\"\"\"

CONTRACT EXCERPTS:
\"\"\"
{contract_context}
\"\"\"

USER REQUEST / QUESTION:
\"{question}\"

INSTRUCTIONS:
1. Answer accurately based on the statutory authorities and contract excerpts, applying Indian legal context (Indian Contract Act 1872, Arbitration Act 1996, INR ₹ currency norms).
2. If drafting or modifying a clause (e.g., "Draft an arbitration clause", "Add an indemnity clause", "Draft confidentiality clause"):
   - Provide complete, attorney-grade legal clauses fully enforceable in Indian High Courts and Supreme Court of India.
   - For employment non-competes, advise that post-employment restrictions are void under Section 27 of ICA 1872, and draft a robust Non-Solicitation and Confidentiality provision instead.
3. If doing legal research:
   - Provide a structured Legal Research Memo citing relevant Sections of Indian Acts and landmark Supreme Court precedents.

ANSWER:"""

    sources = [
        {"text": c["text"], "chunk_index": c["chunk_index"]}
        for c in contract_chunks
    ] if contract_chunks else []

    return prompt, sources, False, ""


# ─── NON-STREAMING QUERY ──────────────────────────────────────────────────────

async def query_contract(contract_id: str, question: str) -> dict:
    """
    Answer a user's prompt using Lexora Origin v1 RAG intelligence (Non-streaming).
    """
    prompt, sources, is_greeting, greeting_text = await _build_rag_context_and_prompt(contract_id, question)

    if is_greeting:
        return {
            "answer": greeting_text,
            "sources": [],
        }

    answer = await _call_ollama_chat(prompt)

    return {
        "answer": answer,
        "sources": sources,
    }


# ─── REAL-TIME TOKEN STREAMING GENERATOR ──────────────────────────────────────

async def stream_query_contract(contract_id: str, question: str) -> AsyncGenerator[str, None]:
    """
    Yields Server-Sent Events (SSE) for real-time token streaming.
    """
    prompt, sources, is_greeting, greeting_text = await _build_rag_context_and_prompt(contract_id, question)

    # 1. Emit Sources First
    yield f"data: {json.dumps({'type': 'sources', 'sources': sources})}\n\n"

    # 2. Emit Greeting Tokens if Greeting
    if is_greeting:
        for word in greeting_text.split(" "):
            yield f"data: {json.dumps({'type': 'token', 'token': word + ' '})}\n\n"
        yield f"data: {json.dumps({'type': 'done'})}\n\n"
        return

    # 3. Stream Ollama Generated Tokens
    async for token in _stream_ollama_chat(prompt):
        yield f"data: {json.dumps({'type': 'token', 'token': token})}\n\n"

    # 4. Finish
    yield f"data: {json.dumps({'type': 'done'})}\n\n"


# ─── HELPERS: Ollama API Calls ────────────────────────────────────────────────

async def _call_ollama_chat(prompt: str) -> str:
    """Send prompt to Ollama model (non-streaming)."""
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


async def _stream_ollama_chat(prompt: str) -> AsyncGenerator[str, None]:
    """Stream tokens directly from Ollama as they are generated."""
    async with httpx.AsyncClient(timeout=180.0) as client:
        async with client.stream(
            "POST",
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_CHAT_MODEL,
                "prompt": prompt,
                "stream": True,
            },
        ) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if line:
                    try:
                        chunk = json.loads(line)
                        token = chunk.get("response", "")
                        if token:
                            yield token
                        if chunk.get("done", False):
                            break
                    except Exception:
                        pass
