"""
inspect_chroma.py
Quick utility to inspect all collections, stored chunks, and vector counts in ChromaDB.
Run directly with: python3 inspect_chroma.py
"""

import chromadb
import os

db_path = os.getenv("CHROMA_DB_PATH", "./chroma_db")
client = chromadb.PersistentClient(path=db_path)

collections = client.list_collections()
print(f"\n========================================================")
print(f"📦 TOTAL INDEXED CONTRACTS IN CHROMADB: {len(collections)}")
print(f"========================================================")

if not collections:
    print("No collections found in local ./chroma_db folder.")
    print("Note: If running in Docker, data lives in the Docker volume.")

for col in collections:
    count = col.count()
    print(f"\n📄 Collection: {col.name}")
    print(f"   📊 Stored Chunks: {count}")
    
    # Retrieve sample chunks
    data = col.get(limit=3, include=["documents", "metadatas"])
    if data["documents"]:
        print("   🔍 Sample Chunks:")
        for idx, doc in enumerate(data["documents"]):
            chunk_id = data["ids"][idx]
            meta = data["metadatas"][idx] if data["metadatas"] else {}
            preview = doc.replace("\n", " ")[:100]
            print(f"      • [{chunk_id}] (Idx {meta.get('chunk_index', idx)}): \"{preview}...\"")

print(f"\n========================================================\n")
