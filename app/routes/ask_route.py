"""
ask_route.py
POST /ask — Ask a question about a contract.

Called by your Node.js backend when user submits a question in the chat UI.
Searches ChromaDB for relevant chunks and generates an answer using Ollama.
"""

from fastapi import APIRouter, HTTPException
from app.models.schemas import AskRequest, AskResponse, SourceChunk
from app.services.rag import query_contract

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
async def ask_question_route(body: AskRequest):
    """
    Answer a user's question about a specific contract using RAG.

    Request body:
        contract_id: str — Which contract to search in
        question:    str — The user's question

    Returns:
        answer:  str         — AI generated answer
        sources: list        — Relevant chunks used to generate the answer
    """
    if not body.question or not body.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if not body.contract_id or not body.contract_id.strip():
        raise HTTPException(status_code=400, detail="contract_id is required")

    result = await query_contract(
        contract_id=body.contract_id,
        question=body.question,
    )

    return AskResponse(
        answer=result["answer"],
        sources=[
            SourceChunk(text=s["text"], chunk_index=s["chunk_index"])
            for s in result["sources"]
        ],
    )
