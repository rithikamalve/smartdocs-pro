from services import summarizer_groq, classifier_groq, classifier_hf
from services import translator, ocr, rag_qa  

def summarize(text):
    # Use only Groq for summarization
    return summarizer_groq.summarize(text)

def classify(text):
    try:
        return classifier_groq.classify(text)
    except Exception:
        return classifier_hf.classify(text)

def translate(text, target_lang):
    return translator.translate_text(text, target_lang)

def ocr_extract(file_path):
    # Only pytesseract-based OCR is used
    return ocr.ocr_file(file_path)

def rag_answer(file_path, question):
    """
    Answers questions using RAG over the given document.
    """
    return rag_qa.answer_question(file_path, question)  # ✅ route the call to rag_qa
