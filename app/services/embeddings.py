"""
embeddings.py
Calls Ollama locally to convert text into vectors (embeddings).

What is an embedding?
- A list of numbers (e.g. 768 floats) that represent the "meaning" of text
- Similar text = similar numbers
- This is what makes semantic search possible
"""

import httpx
from app.config import OLLAMA_BASE_URL, OLLAMA_EMBED_MODEL


async def get_embedding(text: str) -> list[float]:
    """
    Send text to Ollama and get back a vector (list of floats).

    Args:
        text: The text to embed (a chunk of contract text or a user question)

    Returns:
        A list of floats representing the semantic meaning of the text
    """
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            f"{OLLAMA_BASE_URL}/api/embeddings",
            json={
                "model": OLLAMA_EMBED_MODEL,
                "prompt": text,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["embedding"]  # list of floats e.g. [0.23, -0.87, 0.45, ...]


async def get_embeddings_batch(texts: list[str]) -> list[list[float]]:
    """
    Embed multiple texts one by one.
    (Ollama doesn't support true batch embedding yet, so we call sequentially)

    Args:
        texts: List of text strings to embed

    Returns:
        List of embeddings, one per input text
    """
    embeddings = []
    for text in texts:
        embedding = await get_embedding(text)
        embeddings.append(embedding)
    return embeddings
