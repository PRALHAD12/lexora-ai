"""
index_route.py
POST /index — Index a contract for RAG.

Called by your Node.js backend after a contract is uploaded.
Receives the contract text, chunks it, embeds it, stores in ChromaDB.
"""

from fastapi import APIRouter, HTTPException
from app.models.schemas import IndexRequest, SuccessResponse
from app.services.rag import index_contract

router = APIRouter()


@router.post("/index", response_model=SuccessResponse)
async def index_contract_route(body: IndexRequest):
    """
    Index a contract so it can be searched with RAG.

    Request body:
        contract_id: str  — MongoDB contract ID
        text:        str  — Full extracted text of the contract
        title:       str  — Contract title (optional)
        user_id:     str  — User ID (optional)

    Returns:
        Success message with number of chunks indexed
    """
    if not body.text or not body.text.strip():
        raise HTTPException(status_code=400, detail="Contract text cannot be empty")

    if not body.contract_id or not body.contract_id.strip():
        raise HTTPException(status_code=400, detail="contract_id is required")

    chunks_count = await index_contract(
        contract_id=body.contract_id,
        text=body.text,
        title=body.title or "",
    )

    return SuccessResponse(
        success=True,
        message=f"Contract indexed successfully",
        data={
            "contract_id": body.contract_id,
            "chunks_indexed": chunks_count,
        },
    )
