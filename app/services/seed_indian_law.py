"""
seed_indian_law.py
Pre-indexes Indian Statutory Provisions and Landmark Precedents into ChromaDB collection 'indian_law_knowledge'.
"""

import logging
from app.data.indian_law_corpus import INDIAN_LAW_STATUTES
from app.services.chunker import chunk_text
from app.services.embeddings import get_embeddings_batch
from app.services.vectorstore import _client

logger = logging.getLogger("lexora-rag.seed")

INDIAN_LAW_COLLECTION_NAME = "indian_law_knowledge"


async def seed_indian_law_knowledge(force_reseed: bool = False) -> int:
    """
    Check if 'indian_law_knowledge' collection exists and has chunks.
    If not or if force_reseed=True, chunk all Indian statutes, generate embeddings, and store in ChromaDB.
    """
    try:
        try:
            collection = _client.get_collection(name=INDIAN_LAW_COLLECTION_NAME)
            count = collection.count()
            # If already has full corpus and not force_reseed, skip
            if count >= len(INDIAN_LAW_STATUTES) * 2 and not force_reseed:
                logger.info(f"Indian Law Knowledge Base already indexed ({count} chunks).")
                return count
            elif count > 0 or force_reseed:
                _client.delete_collection(name=INDIAN_LAW_COLLECTION_NAME)
        except Exception:
            pass

        collection = _client.create_collection(
            name=INDIAN_LAW_COLLECTION_NAME,
            metadata={"description": "Indian Statutory Laws, Supreme Court Precedents & Contract Templates", "hnsw:space": "cosine"}
        )

        all_chunks = []
        for stat in INDIAN_LAW_STATUTES:
            chunks = chunk_text(stat["text"], chunk_size=450, overlap=90)
            for c in chunks:
                c["act"] = stat["act"]
                c["section"] = stat["section"]
                c["title"] = stat["title"]
                c["category"] = stat.get("category", "General")
                all_chunks.append(c)

        if not all_chunks:
            return 0

        chunk_texts = [c["text"] for c in all_chunks]
        embeddings = await get_embeddings_batch(chunk_texts)

        ids = [f"ind_law_chunk_{i}" for i in range(len(all_chunks))]
        metadatas = [
            {
                "chunk_index": c["chunk_index"],
                "act": c["act"],
                "section": c["section"],
                "title": c["title"],
                "category": c["category"],
            }
            for c in all_chunks
        ]

        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=chunk_texts,
            metadatas=metadatas,
        )

        logger.info(f"Successfully seeded {len(all_chunks)} Indian Law Statutory Chunks into ChromaDB!")
        return len(all_chunks)

    except Exception as e:
        logger.error(f"Failed to seed Indian Law Knowledge Base: {e}")
        return 0


def search_indian_law_statutes(query_embedding: list[float], top_k: int = 4) -> list[dict]:
    """
    Search the 'indian_law_knowledge' collection for statutes/precedents relevant to the query.
    """
    try:
        collection = _client.get_collection(name=INDIAN_LAW_COLLECTION_NAME)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=min(top_k, collection.count()),
            include=["documents", "metadatas", "distances"],
        )

        chunks = []
        for i, doc in enumerate(results["documents"][0]):
            meta = results["metadatas"][0][i]
            chunks.append({
                "text": doc,
                "act": meta.get("act", ""),
                "section": meta.get("section", ""),
                "title": meta.get("title", ""),
                "category": meta.get("category", ""),
                "score": 1 - results["distances"][0][i],
            })
        return chunks
    except Exception:
        return []
