from flask import Blueprint, request, jsonify
import time
from services import router
from services.extractor import extract_text
import os

summarize_bp = Blueprint('summarize', __name__)
UPLOAD_FOLDER = '/tmp/smartdocs_uploads'

@summarize_bp.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    doc_id = data.get('document_id')
    ext = data.get('ext')
    if not doc_id or not ext:
        return jsonify({'error': 'Missing document_id or ext'}), 400
    file_path = os.path.join(UPLOAD_FOLDER, f'{doc_id}{ext}')
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    text = extract_text(file_path)
    start = time.time()
    try:
        summary = router.summarize(text)
        elapsed = time.time() - start
        return jsonify({'summary': summary, 'inference_time': elapsed})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 