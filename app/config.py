"""
config.py
Loads all environment variables from .env file.
All other files import settings from here — one central place.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Server
PORT = int(os.getenv("PORT", 8000))

# Ollama
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
OLLAMA_CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "lexora-origin:v1")

# ChromaDB
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")

# Node backend
NODE_BACKEND_URL = os.getenv("NODE_BACKEND_URL", "http://localhost:5000")
