import os

import streamlit as st
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

NOTES_PATH = os.getenv("NOTES_PATH", "data/notes.txt")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)
with open(NOTES_PATH, "r") as f:
    documents = [line.strip() for line in f.readlines()]

doc_embeddings = model.encode(documents)

st.title("AI Semantic Search")

query = st.text_input(
    "Ask anything"
)

if query:
    query_embedding = model.encode([query])

    scores = cosine_similarity(
        query_embedding,
        doc_embeddings
    )[0]

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    for doc, score in ranked[:3]:
        st.write(
            f"{score:.3f} - {doc}"
        )