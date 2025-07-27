import os
from groq import Groq
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings 

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)


def load_documents(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()


def create_vectorstore(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.from_documents(splits, embeddings)
    return vectordb


def answer_question(file_path, question):
    try:
        print(f"📥 Loading document: {file_path}")
        docs = load_documents(file_path)
        print(f"✅ Loaded {len(docs)} documents.")

        vectordb = create_vectorstore(docs)
        print("✅ Vector store created.")

        retriever = vectordb.as_retriever(search_kwargs={"k": 5})
        relevant_docs = retriever.get_relevant_documents(question)
        print(f"✅ Retrieved {len(relevant_docs)} relevant documents.")

        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        messages = [
            {"role": "system", "content": "You are a helpful assistant..."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ]

        response = client.chat.completions.create(
            model="meta-llama/llama-4-maverick-17b-128e-instruct",
            messages=messages,
            temperature=0.2,
            max_tokens=1024,
            top_p=1,
            stream=False,
        )

        print("✅ Got response from Groq.")
        return {
            "question": question,
            "answer": response.choices[0].message.content.strip(),
            "context_snippets": [doc.page_content for doc in relevant_docs],
        }

    except Exception as e:
        print(f"❌ Error in answer_question: {e}")
        raise e
