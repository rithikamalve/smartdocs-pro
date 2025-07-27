# SmartDocs Pro

SmartDocs Pro is an intelligent document understanding system designed to extract, classify, translate, summarize, and answer questions about document content using state-of-the-art AI models. It supports PDFs, DOCX files, images, and scanned text, making it ideal for resumes, reports, and other structured/unstructured documents.

---

## Features

### Document Understanding Capabilities
- **Text Extraction** from PDFs, Word Docs, and scanned images  
- **Multilingual Translation** with Groq-backed LLMs  
- **Document Classification** using Groq and Hugging Face fallback  
- **Summarization** powered by Groq's LLaMA-4 Maverick model  
- **OCR** via Tesseract for image-based documents  
- **RAG-based Question Answering** using vector search and Groq models  

---

## Tech Stack

- **Backend:** Python, Flask, Gunicorn  
- **Frontend:** Streamlit (deployed separately)  
- **LLM Provider:** [Groq](https://groq.com/) (`meta-llama/llama-4-maverick-17b-128e-instruct`)  
- **Embeddings:** HuggingFace `all-MiniLM-L6-v2` with FAISS vector store  
- **OCR Engine:** Tesseract  
- **Document Parsing:** `pdfplumber`, `python-docx`, `pdf2image`  
- **Deployment:** Docker, Render, Streamlit Cloud  

---


## API Overview

| Endpoint       | Method | Description                             |
|----------------|--------|-----------------------------------------|
| `/upload`      | POST   | Upload document for processing          |
| `/translate`   | POST   | Translate extracted text                |
| `/summarize`   | POST   | Summarize document                      |
| `/classify`    | POST   | Classify document type                  |
| `/ocr`         | POST   | Extract text via OCR                    |
| `/rag`         | POST   | Ask questions about uploaded documents  |
| `/status`      | GET    | Health check                            |

---

Contribution
If you’d like to extend the system with more models, languages, or processing capabilities, feel free to fork and submit a PR.

License
MIT License
