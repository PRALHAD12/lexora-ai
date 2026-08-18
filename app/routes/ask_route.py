"""
ask_route.py
POST /api/rag/ask    — Non-streaming Q&A about a contract
POST /api/rag/stream — Real-time token-by-token streaming (SSE) Q&A
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models.schemas import AskRequest, AskResponse, SourceChunk
from app.services.rag import query_contract, stream_query_contract

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
async def ask_question_route(body: AskRequest):
    """
    Answer a user's question about a specific contract using RAG (JSON response).
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


@router.post("/stream")
async def stream_question_route(body: AskRequest):
    """
    Stream real-time tokens for a contract question using Server-Sent Events (SSE).
    """
    if not body.question or not body.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if not body.contract_id or not body.contract_id.strip():
        raise HTTPException(status_code=400, detail="contract_id is required")

    return StreamingResponse(
        stream_query_contract(
            contract_id=body.contract_id,
            question=body.question,
        ),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
