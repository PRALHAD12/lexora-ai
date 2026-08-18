"""
main.py
Entry point for the Lexora RAG Python microservice.

This is a FastAPI server that runs on port 8000.
Your Node.js backend (port 5000) calls this service internally.

Routes:
  POST /api/rag/index        — Index a contract (chunk + embed + store)
  POST /api/rag/ask          — Ask a question about a contract (RAG query)
  POST /api/rag/generate     — General AI generation fallback
  GET  /api/rag/stats        — Vector database stats
  GET  /api/rag/collections  — List all indexed contract collections
  GET  /health               — Health check
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.index_route import router as index_router
from app.routes.ask_route import router as ask_router
from app.routes.generate_route import router as generate_router
from app.routes.debug_route import router as debug_router
from app.config import PORT, NODE_BACKEND_URL

# ─── Create FastAPI App ───────────────────────────────────────────────────────
app = FastAPI(
    title="Lexora RAG Service",
    description="Python microservice for RAG-powered contract Q&A using Ollama + ChromaDB",
    version="1.0.0",
)

# ─── CORS — Allow Node.js backend to call this service ───────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[NODE_BACKEND_URL, "http://localhost:3000", "http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Routes ──────────────────────────────────────────────────────────────────
app.include_router(index_router, prefix="/api/rag", tags=["RAG"])
app.include_router(ask_router, prefix="/api/rag", tags=["RAG"])
app.include_router(generate_router, prefix="/api/rag", tags=["RAG"])
app.include_router(debug_router, prefix="/api/rag", tags=["ChromaDB Inspection"])


# ─── Health Check ────────────────────────────────────────────────────────────
@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "service": "Lexora RAG Service",
        "version": "1.0.0",
    }


# ─── Run ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
