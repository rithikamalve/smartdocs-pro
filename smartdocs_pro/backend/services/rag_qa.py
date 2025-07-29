import os
import faiss
import numpy as np
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

# Load env + model once
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)
model = SentenceTransformer("all-MiniLM-L6-v2")  # ~80MB model

def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def create_vector_index(chunks):
    vectors = model.encode(chunks, convert_to_numpy=True)
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index, vectors, chunks

def answer_question(text, question, k=5):
    print(f"📥 Text length: {len(text)}")
    chunks = split_text(text)
    index, vectors, raw_chunks = create_vector_index(chunks)

    print("✅ FAISS index built.")
    q_vec = model.encode([question])
    _, I = index.search(q_vec, k)
    relevant_chunks = [raw_chunks[i] for i in I[0]]

    context = "\n\n".join(relevant_chunks)
    prompt = [
        {
            "role": "system",
            "content": "You are a helpful assistant that answers questions using the context provided.",
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}",
        },
    ]

    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=prompt,
        temperature=0.2,
        max_tokens=1024,
        top_p=1,
    )

    return {
        "question": question,
        "answer": response.choices[0].message.content.strip(),
        "context_snippets": relevant_chunks,
    }
