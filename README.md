# 🧠 Migration Law Semantic Search

This project uses **ChromaDB** and **OpenAI Embeddings** to enable natural language search across Australian migration law documents.

## 🔍 Features
- Semantic search over `.txt` files using `text-embedding-3-small`
- Embedding via OpenAI
- Vector storage via ChromaDB (persistent)
- Modular design (with `.env` and `services/`)

## 📂 Structure
- `data/`: migration law documents
- `services/chroma_engine.py`: all ChromaDB + embedding logic
- `main.py`: run this to build index and query documents

## 🚀 Getting Started

1. Clone the repo:
```bash
git clone https://github.com/atefehmalaee/migration-law-semantic-search.git
cd migration-law-semantic-search
