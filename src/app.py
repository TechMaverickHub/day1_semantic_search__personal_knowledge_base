import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

NOTES_PATH = os.getenv("NOTES_PATH", "data/notes.txt")

with open(NOTES_PATH, "r") as f:
    documents = [line.strip() for line in f.readlines()]

doc_embeddings = model.encode(documents)

print("\nAI Semantic Search")
print("-" * 50)

while True:
    query = input("\nAsk something: ")

    if query.lower() == "exit":
        break

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

    print("\nTop Matches:\n")

    for doc, score in ranked[:3]:
        print(f"{score:.3f} | {doc}")
