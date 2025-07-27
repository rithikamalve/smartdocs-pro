from flask import Blueprint, request, jsonify
import os
import uuid

upload_bp = Blueprint('upload', __name__)
UPLOAD_FOLDER = '/tmp/smartdocs_uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ['.pdf', '.docx']:
        return jsonify({'error': 'Unsupported file type'}), 400
    doc_id = str(uuid.uuid4())
    save_path = os.path.join(UPLOAD_FOLDER, f'{doc_id}{ext}')
    file.save(save_path)
    return jsonify({'document_id': doc_id, 'filename': file.filename}) 