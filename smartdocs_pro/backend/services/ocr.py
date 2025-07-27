import pytesseract
from PIL import Image, ImageOps
import pdfplumber
import os

def preprocess_image(image):
    """
    Converts image to grayscale and applies auto contrast
    for improved OCR accuracy. Extend with denoising if needed.
    """
    gray = ImageOps.grayscale(image)
    enhanced = ImageOps.autocontrast(gray)
    return enhanced

def ocr_file(file_path, lang='eng'):
    """
    Performs OCR on images and PDFs.
    
    Args:
        file_path (str): Path to the file
        lang (str): Language code for OCR, default 'eng'
        
    Returns:
        str: Extracted text
    """
    ext = os.path.splitext(file_path)[1].lower()
    text = ''
    
    try:
        if ext in ['.png', '.jpg', '.jpeg']:
            image = Image.open(file_path)
            processed_image = preprocess_image(image)
            text = pytesseract.image_to_string(processed_image, lang=lang)
        
        elif ext == '.pdf':
            with pdfplumber.open(file_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    img = page.to_image(resolution=300)
                    pil_img = preprocess_image(img.original)
                    page_text = pytesseract.image_to_string(pil_img, lang=lang)
                    text += f"\n--- Page {i+1} ---\n{page_text}\n"
        
        else:
            raise ValueError(f"Unsupported file type for OCR: {ext}")
        
    except Exception as e:
        raise RuntimeError(f"OCR processing failed for {file_path}: {e}")
    
    return text
