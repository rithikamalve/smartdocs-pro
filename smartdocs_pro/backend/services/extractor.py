import pdfplumber
import docx
import os

def extract_text(file_path):
    """
    Extracts text from PDF or DOCX files.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        str: Extracted text
    
    Raises:
        ValueError: If file type is unsupported
        RuntimeError: If extraction fails
    """
    ext = os.path.splitext(file_path)[1].lower()
    text = ''
    
    try:
        if ext == '.pdf':
            with pdfplumber.open(file_path) as pdf:
                pages_text = []
                for i, page in enumerate(pdf.pages):
                    page_text = page.extract_text() or ''
                    pages_text.append(f"\n--- Page {i+1} ---\n{page_text}")
                text = '\n'.join(pages_text)
        
        elif ext == '.docx':
            doc = docx.Document(file_path)
            # Filter out empty paragraphs for cleaner output
            paragraphs = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
            text = '\n'.join(paragraphs)
        
        else:
            raise ValueError(f"Unsupported file type for extraction: {ext}")
    
    except Exception as e:
        raise RuntimeError(f"Text extraction failed for {file_path}: {e}")
    
    return text
