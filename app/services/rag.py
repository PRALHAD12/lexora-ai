"""
rag.py
Core RAG logic — ties everything together.

This file has two main jobs:
1. index_contract()  — called when a contract is uploaded
2. query_contract()  — called when user asks a question
"""

import httpx
from app.config import OLLAMA_BASE_URL, OLLAMA_CHAT_MODEL
from app.services.chunker import chunk_text
from app.services.embeddings import get_embedding, get_embeddings_batch
from app.services.vectorstore import save_chunks, search_similar_chunks


# ─── INDEXING ────────────────────────────────────────────────────────────────

async def index_contract(contract_id: str, text: str, title: str = "") -> int:
    """
    Index a contract for RAG.

    Steps:
    1. Split the contract text into chunks
    2. Generate an embedding for each chunk
    3. Save chunks + embeddings to ChromaDB

    Args:
        contract_id: MongoDB contract ID
        text:        Full extracted text of the contract
        title:       Contract title (for logging)

    Returns:
        Number of chunks indexed
    """
    # Step 1 — Chunk the text
    chunks = chunk_text(text, chunk_size=500, overlap=100)

    if not chunks:
        return 0

    # Step 2 — Embed all chunks
    chunk_texts = [c["text"] for c in chunks]
    embeddings = await get_embeddings_batch(chunk_texts)

    # Step 3 — Save to ChromaDB
    save_chunks(contract_id, chunks, embeddings)

    return len(chunks)


# ─── QUERYING ─────────────────────────────────────────────────────────────────

async def query_contract(contract_id: str, question: str) -> dict:
    """
    Answer a user's question using RAG.

    Steps:
    1. Embed the user's question
    2. Search ChromaDB for top-5 most relevant chunks
    3. Build a prompt with the chunks as context
    4. Send prompt to Ollama chat model
    5. Return the answer + the source chunks used

    Args:
        contract_id: Which contract to search in
        question:    The user's question

    Returns:
        dict with keys: answer (str), sources (list)
    """
    # Step 1 — Embed the question
    query_embedding = await get_embedding(question)

    # Step 2 — Find top-5 most relevant chunks
    relevant_chunks = search_similar_chunks(
        contract_id=contract_id,
        query_embedding=query_embedding,
        top_k=5,
    )

    if not relevant_chunks:
        return {
            "answer": "I could not find any relevant content in this contract to answer your question.",
            "sources": [],
        }

    # Step 3 — Build context from the retrieved chunks
    context = "\n\n---\n\n".join(
        [f"[Excerpt {i+1}]:\n{chunk['text']}" for i, chunk in enumerate(relevant_chunks)]
    )

    # Step 4 — Build the prompt
    prompt = f"""You are a legal AI assistant for Lexora, a contract analysis platform.
Answer the user's question based ONLY on the contract excerpts provided below.
Be concise, clear, and professional.
If the answer is not found in the excerpts, say exactly: "I could not find this information in the provided contract."
Do NOT make up or guess information.

CONTRACT EXCERPTS:
{context}

USER QUESTION: {question}

ANSWER:"""

    # Step 5 — Call Ollama chat model
    answer = await _call_ollama_chat(prompt)

    return {
        "answer": answer,
        "sources": [
            {"text": c["text"], "chunk_index": c["chunk_index"]}
            for c in relevant_chunks
        ],
    }


# ─── HELPER: Call Ollama Chat ─────────────────────────────────────────────────

async def _call_ollama_chat(prompt: str) -> str:
    """
    Send a prompt to Ollama and get back the generated text response.
    """
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_CHAT_MODEL,
                "prompt": prompt,
                "stream": False,  # get the full response at once
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["response"].strip()
