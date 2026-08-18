"""
vectorstore.py
Handles saving and searching vectors using ChromaDB.

What is ChromaDB?
- A local vector database that runs on your machine
- Stores text chunks + their vectors (embeddings)
- Can find the most "similar" chunks to any query vector
- Data is saved to disk in the ./chroma_db folder
"""

import chromadb
from app.config import CHROMA_DB_PATH

# Initialize ChromaDB client — saves data to disk
_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)


def _get_collection(contract_id: str):
    """
    Get or create a ChromaDB collection for a specific contract.
    Each contract gets its own isolated collection.
    Collection name must be alphanumeric + underscores, so we sanitize.
    """
    collection_name = f"contract_{contract_id.replace('-', '_')}"
    return _client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},  # use cosine similarity for search
    )


def save_chunks(contract_id: str, chunks: list[dict], embeddings: list[list[float]]):
    """
    Save contract chunks and their embeddings to ChromaDB.

    Args:
        contract_id: MongoDB contract ID (used to name the collection)
        chunks:      List of chunk dicts from chunker.py
        embeddings:  List of embedding vectors from embeddings.py
    """
    collection = _get_collection(contract_id)

    # Clear existing data for this contract (in case of re-indexing)
    existing = collection.get()
    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    # Add all chunks with their embeddings
    collection.add(
        ids=[f"chunk_{c['chunk_index']}" for c in chunks],
        documents=[c["text"] for c in chunks],
        embeddings=embeddings,
        metadatas=[
            {
                "chunk_index": c["chunk_index"],
                "start_index": c["start_index"],
                "end_index": c["end_index"],
            }
            for c in chunks
        ],
    )


def search_similar_chunks(
    contract_id: str, query_embedding: list[float], top_k: int = 5
) -> list[dict]:
    """
    Find the top-K chunks most similar to the query embedding.

    Args:
        contract_id:     Which contract to search in
        query_embedding: The embedding of the user's question
        top_k:           How many chunks to return (default 5)

    Returns:
        List of dicts with keys: text, chunk_index, score
    """
    collection = _get_collection(contract_id)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),  # can't exceed total chunks
        include=["documents", "metadatas", "distances"],
    )

    chunks = []
    for i, doc in enumerate(results["documents"][0]):
        chunks.append(
            {
                "text": doc,
                "chunk_index": results["metadatas"][0][i]["chunk_index"],
                "score": 1 - results["distances"][0][i],  # convert distance to similarity score
            }
        )

    return chunks


def delete_contract_index(contract_id: str):
    """
    Delete all indexed chunks for a contract (e.g. when contract is deleted).
    """
    collection_name = f"contract_{contract_id.replace('-', '_')}"
    try:
        _client.delete_collection(name=collection_name)
    except Exception:
        pass  # collection may not exist, that's fine
