from flask import Blueprint, jsonify
import os

status_bp = Blueprint('status', __name__)

@status_bp.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'ok', 'version': os.environ.get('SMARTDOCS_VERSION', 'dev')}) 