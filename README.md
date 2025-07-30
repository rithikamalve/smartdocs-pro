# 📄 SmartDocs Pro

**SmartDocs Pro** is an intelligent document understanding system designed to extract, classify, translate, summarize, and answer questions about document content using state-of-the-art AI models.  
It supports **PDFs**, **DOCX files**, **images**, and **scanned text**, making it ideal for resumes, reports, and both structured and unstructured documents.

---

## ✨ Features

### 🧠 Document Understanding Capabilities
- 📄 Text Extraction from PDFs, Word Docs, and scanned images
- 🌍 Multilingual Translation (Groq-backed LLMs)
- 🗂️ Document Classification (Groq + Hugging Face fallback)
- ✂️ Summarization (LLaMA-4 Maverick via Groq)
- 🖼️ OCR via Tesseract for image-based documents
- 🔎 RAG-based Question Answering using vector search

---

## ⚙️ Tech Stack

| Layer             | Tools / Frameworks |
|------------------|--------------------|
| **Backend**       | Python, Flask, Gunicorn |
| **Frontend**      | Streamlit (deployed separately) |
| **LLM Provider**  | Groq (LLaMA-4 Maverick) |
| **Embeddings**    | HuggingFace `all-MiniLM-L6-v2`, FAISS |
| **OCR Engine**    | Tesseract |
| **Parsing Tools** | `pdfplumber`, `python-docx`, `pdf2image` |
| **Deployment**    | Docker, Render, Streamlit Cloud |

---

## 🔌 API Overview

| Endpoint    | Method | Description                           |
|-------------|--------|---------------------------------------|
| `/upload`   | POST   | Upload document for processing        |
| `/translate`| POST   | Translate extracted text              |
| `/summarize`| POST   | Summarize document                    |
| `/classify` | POST   | Classify document type                |
| `/ocr`      | POST   | Extract text via OCR                  |
| `/rag`      | POST   | Ask questions about uploaded documents |
| `/status`   | GET    | Health check route                    |

---

## 📄 License

This project is licensed under the **MIT License**.
