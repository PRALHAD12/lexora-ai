"""
generate_route.py
POST /api/rag/generate — General AI text generation (no RAG, no vector search).

Used as a fallback when no contractId is available (e.g. new unsaved contracts).
Takes a raw prompt and sends it directly to Ollama chat model.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rag import _call_ollama_chat

router = APIRouter()


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    answer: str


@router.post("/generate", response_model=GenerateResponse)
async def generate_route(body: GenerateRequest):
    """
    General AI generation — sends prompt directly to Ollama (no vector search).

    Request body:
        prompt: str — The full prompt to send to the LLM

    Returns:
        answer: str — The AI generated response
    """
    if not body.prompt or not body.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    answer = await _call_ollama_chat(body.prompt.strip())

    return GenerateResponse(answer=answer)
