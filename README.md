# AI Semantic Search Engine

A lightweight semantic search application that uses Sentence Transformers and cosine similarity to retrieve the most relevant notes based on meaning rather than exact keyword matches.

This project was built as part of my transition from Backend Engineering to AI Engineering, focusing on practical applications of embeddings, semantic search, and retrieval systems.

---

## Why This Project?

Traditional search relies on exact keyword matching.

### Example

**Query**

```text
background jobs
```

Traditional keyword search may fail if the document contains:

```text
Using Celery with Redis for asynchronous task processing
```

Semantic search understands the meaning behind the query and retrieves relevant results even when exact words do not match.

This concept forms the foundation of:

- Retrieval-Augmented Generation (RAG)
- AI Assistants
- Knowledge Base Search
- Recommendation Systems
- Vector Databases

---

## Features

- Semantic search using embeddings
- Cosine similarity ranking
- Interactive command-line interface
- Streamlit web interface
- Local knowledge base search
- Modern Python dependency management using UV

---

## Tech Stack

- Python 3.12+
- Sentence Transformers
- Scikit-Learn
- Streamlit
- UV

---

## Project Structure

```text
day1-semantic-search/
│
├── data/
│   └── notes.txt
│
├── src/
│   ├── app.py
│   └── streamlit_app.py
│
├── docs/
│   └── learning-notes.md
│
├── screenshots/
│
├── README.md
├── pyproject.toml
└── uv.lock
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd day1-semantic-search
```

Install dependencies:

```bash
uv sync
```

---

## Run CLI Version

```bash
uv run src/app.py
```

### Example

```text
Ask something:
vector database

Top Matches

0.89 | Building RAG applications using LangChain and FAISS
0.74 | Prompt engineering best practices
0.61 | FastAPI production deployment guide
```

---

## Run Streamlit Version

```bash
uv run streamlit run src/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

## Sample Knowledge Base

Example notes:

```text
Optimizing Django ORM queries with select_related

Using Celery and Redis for asynchronous processing

Implementing JWT authentication in Django REST Framework

Building Retrieval-Augmented Generation systems

Deploying FastAPI applications with Docker

PostgreSQL indexing best practices
```

---

## How It Works

### Step 1: Load Documents

Documents are loaded from the local knowledge base.

### Step 2: Generate Embeddings

Each document is converted into a dense vector representation using a pre-trained Sentence Transformer model.

### Step 3: Encode User Query

The search query is converted into an embedding using the same model.

### Step 4: Calculate Similarity

Cosine similarity is used to compare the query vector against all document vectors.

### Step 5: Return Top Matches

Results are ranked by similarity score and returned to the user.

---

## Example Queries

### Query

```text
background jobs
```

### Result

```text
Using Celery and Redis for asynchronous processing
```

### Query

```text
deploy python api
```

### Result

```text
Deploying FastAPI applications with Docker
```

### Query

```text
vector database
```

### Result

```text
Building Retrieval-Augmented Generation systems
```

---

## Concepts Learned

- Embeddings
- Vector Representations
- Semantic Search
- Cosine Similarity
- Information Retrieval
- Knowledge Search Systems

---

## Future Improvements

- FAISS Vector Database
- PDF Document Ingestion
- Multi-file Knowledge Base
- Hybrid Search (Keyword + Semantic)
- RAG Pipeline Integration
- FastAPI Backend
- Docker Deployment

---

## Interview Talking Points

### What problem does this solve?

It enables semantic retrieval of information based on meaning rather than exact keyword matching.

### Why use embeddings?

Embeddings capture semantic relationships between text and allow efficient similarity-based retrieval.

### Why cosine similarity?

Cosine similarity measures how closely two vectors point in the same direction, making it effective for comparing embeddings.

### How does this relate to RAG?

Semantic retrieval is the first stage of a RAG pipeline. Retrieved documents are later passed to an LLM to generate grounded responses.

---

## Learning Journey

This repository is part of my AI Engineering learning journey, where I am building practical projects around:

- Machine Learning
- Generative AI
- RAG Systems
- Vector Databases
- AI Application Development
- Production AI Systems

### Roadmap

- [x] Semantic Search
- [ ] FAISS Integration
- [ ] PDF Processing
- [ ] RAG Pipeline
- [ ] FastAPI Backend
- [ ] Docker Deployment

---

## Author

**Abhiroop Bhattacharyya**

Backend Engineer → AI Engineer

- Python
- Django
- FastAPI
- Generative AI
- RAG
- Vector Databases

---

⭐ If you found this project useful, consider giving it a star.