from flask import Blueprint, request, jsonify
import time
from services.extractor import extract_text
from services.ocr import ocr_file
import os

ocr_bp = Blueprint('ocr', __name__)
UPLOAD_FOLDER = '/tmp/smartdocs_uploads'

@ocr_bp.route('/ocr', methods=['POST'])
def ocr():
    data = request.json
    doc_id = data.get('document_id')
    ext = data.get('ext')
    if not doc_id or not ext:
        return jsonify({'error': 'Missing document_id or ext'}), 400
    file_path = os.path.join(UPLOAD_FOLDER, f'{doc_id}{ext}')
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    start = time.time()
    try:
        # Try text extraction first
        try:
            text = extract_text(file_path)
        except Exception:
            text = ''
        if not text.strip():
            text = ocr_file(file_path)
        elapsed = time.time() - start
        return jsonify({'ocr_text': text, 'inference_time': elapsed})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 