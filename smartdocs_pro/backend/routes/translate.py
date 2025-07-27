from flask import Blueprint, request, jsonify
import time
from services.translator import translate_text
from services.extractor import extract_text
import os

translate_bp = Blueprint('translate', __name__)
UPLOAD_FOLDER = '/tmp/smartdocs_uploads'

@translate_bp.route('/translate', methods=['POST'])
def translate():
    data = request.json
    doc_id = data.get('document_id')
    ext = data.get('ext')
    target_lang = data.get('target_lang')
    if not doc_id or not ext or not target_lang:
        return jsonify({'error': 'Missing document_id, ext, or target_lang'}), 400
    file_path = os.path.join(UPLOAD_FOLDER, f'{doc_id}{ext}')
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    text = extract_text(file_path)
    start = time.time()
    try:
        translation = translate_text(text, target_lang)
        elapsed = time.time() - start
        return jsonify({'translation': translation, 'inference_time': elapsed})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 