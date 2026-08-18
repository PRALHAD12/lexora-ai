"""
schemas.py
Defines the shape of all API request and response data.
Think of these as TypeScript interfaces but in Python.
"""

from pydantic import BaseModel
from typing import Optional


# ─── Request: Index a contract ─────────────────────────────────────────────
class IndexRequest(BaseModel):
    contract_id: str          # MongoDB contract ID from your Node.js backend
    text: str                 # Full extracted text of the contract
    title: Optional[str] = "" # Contract title (optional, for metadata)
    user_id: Optional[str] = "" # User ID (optional, for filtering)


# ─── Request: Ask a question ────────────────────────────────────────────────
class AskRequest(BaseModel):
    contract_id: str          # Which contract to search in
    question: str             # The user's question


# ─── Response: Source chunk returned with the answer ────────────────────────
class SourceChunk(BaseModel):
    text: str                 # The chunk text that was used to answer
    chunk_index: int          # Position of this chunk in the document


# ─── Response: Answer to a question ─────────────────────────────────────────
class AskResponse(BaseModel):
    answer: str               # The AI generated answer
    sources: list[SourceChunk] # The chunks that were used


# ─── Response: Generic success message ──────────────────────────────────────
class SuccessResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
