"""
chunker.py
Splits a large contract text into smaller overlapping chunks.

Why do we chunk?
- LLMs have a token limit — they can't read a 20-page contract at once
- Smaller chunks = better search accuracy
- Overlap prevents sentences from being cut in half at chunk boundaries
"""


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[dict]:
    """
    Split text into overlapping chunks.

    Args:
        text:       Full contract text
        chunk_size: Max characters per chunk (default 500)
        overlap:    Characters shared between adjacent chunks (default 100)

    Returns:
        List of dicts with keys: chunk_index, text, start_index, end_index
    """
    if not text or not text.strip():
        return []

    chunks = []
    start = 0
    chunk_index = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk_text_slice = text[start:end].strip()

        if chunk_text_slice:  # skip empty chunks
            chunks.append({
                "chunk_index": chunk_index,
                "text": chunk_text_slice,
                "start_index": start,
                "end_index": end,
            })
            chunk_index += 1

        start += chunk_size - overlap  # slide forward with overlap

    return chunks
