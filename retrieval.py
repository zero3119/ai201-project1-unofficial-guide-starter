import json
import chromadb
from sentence_transformers import SentenceTransformer

CHUNKS_FILE = "chunks.json"
DB_DIR = "chroma_db"
COLLECTION_NAME = "utep_food"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=DB_DIR)
collection = client.get_or_create_collection(name=COLLECTION_NAME)


def load_chunks():
    with open(CHUNKS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def build_vector_store():
    chunks = load_chunks()

    ids = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f"chunk_{i}")
        documents.append(chunk["text"])
        metadatas.append({
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"]
        })

    embeddings = model.encode(documents).tolist()

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(documents)} chunks in ChromaDB.")


def retrieve(query, k=4):
    query_embedding = model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    retrieved = []

    for i in range(len(results["documents"][0])):
        retrieved.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "chunk_id": results["metadatas"][0][i]["chunk_id"],
            "distance": results["distances"][0][i]
        })

    return retrieved


if __name__ == "__main__":
    build_vector_store()

    test_questions = [
        "What are Miner Bucks?",
        "Is Einsten bagels open during summer?",
        "Can meal plans be refunded?"
    ]

    for question in test_questions:
        print("\n" + "=" * 60)
        print("QUERY:", question)

        results = retrieve(question, k=4)

        for result in results:
            print("-" * 60)
            print("Distance:", result["distance"])
            print("Source:", result["source"])
            print("Chunk ID:", result["chunk_id"])
            print(result["text"])