"""
debug_route.py
Provides inspection & debugging endpoints for viewing ChromaDB data.
"""

from fastapi import APIRouter, HTTPException
from app.services.vectorstore import (
    list_all_collections,
    get_contract_chunks,
    get_chroma_stats,
    delete_contract_index,
)

router = APIRouter()


@router.get("/stats", tags=["ChromaDB Inspection"])
async def get_stats():
    """
    Get overall vector database statistics (total contracts, total chunks).
    """
    return {
        "success": True,
        "data": get_chroma_stats(),
    }


@router.get("/collections", tags=["ChromaDB Inspection"])
async def get_collections():
    """
    List all contract collections stored in ChromaDB and their chunk counts.
    """
    collections = list_all_collections()
    return {
        "success": True,
        "total_contracts": len(collections),
        "collections": collections,
    }


@router.get("/collections/{contract_id}", tags=["ChromaDB Inspection"])
async def get_collection_chunks(contract_id: str, limit: int = 50):
    """
    View all text chunks and metadata for a specific contract.
    """
    if not contract_id:
        raise HTTPException(status_code=400, detail="contract_id is required")

    result = get_contract_chunks(contract_id, limit=limit)
    return {
        "success": True,
        "data": result,
    }


@router.delete("/collections/{contract_id}", tags=["ChromaDB Inspection"])
async def delete_collection(contract_id: str):
    """
    Delete all indexed chunks for a contract.
    """
    delete_contract_index(contract_id)
    return {
        "success": True,
        "message": f"Collection for contract {contract_id} deleted successfully",
    }
