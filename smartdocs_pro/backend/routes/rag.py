from flask import Blueprint, request, jsonify
import os
from services.rag_qa import answer_question

rag_bp = Blueprint("rag", __name__)
UPLOAD_FOLDER = "/tmp/smartdocs_uploads"

@rag_bp.route("/rag", methods=["POST"])
def rag_qa():
    data = request.json
    text = data.get("text")
    question = data.get("question")

    if not text or not question:
        return jsonify({"error": "Missing text or question"}), 400

    try:
        result = answer_question(text, question)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

