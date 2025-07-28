from flask import Blueprint, request, jsonify
import os
from services.rag_qa import answer_question

rag_bp = Blueprint("rag", __name__)
UPLOAD_FOLDER = "/tmp/smartdocs_uploads"

@rag_bp.route("/rag", methods=["POST"])
def rag():
    data = request.json
    doc_id = data.get("document_id")
    ext = data.get("ext")
    question = data.get("question")

    if not doc_id or not ext or not question:
        return jsonify({"error": "Missing document_id, ext, or question"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, f"{doc_id}{ext}")
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    try:
        result = answer_question(file_path, question)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
