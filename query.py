import os
from dotenv import load_dotenv
from groq import Groq
from retrieval import retrieve

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask(question):
    retrieved_chunks = retrieve(question, k=4)

    context = "\n\n".join(
        f"Source: {chunk['source']}\nText: {chunk['text']}"
        for chunk in retrieved_chunks
    )

    prompt = f"""
Answer the user's question using ONLY the context below.

If the context does not contain the answer, say:
"I don't have enough information on that."

Do not use outside knowledge.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a grounded RAG assistant. Only answer from retrieved context."},
            {"role": "user", "content": prompt}
        ]
    )

    sources = sorted(set(chunk["source"] for chunk in retrieved_chunks))

    return {
    "answer":  response.choices[0].message.content,
    "sources": sources,
    "chunks": retrieved_chunks
}