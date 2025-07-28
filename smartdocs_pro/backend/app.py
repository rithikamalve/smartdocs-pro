from flask import Flask
from flask_cors import CORS
from config import load_config
import os

def create_app():
    app = Flask(__name__)
    CORS(app)
    load_config(app)

    # Register blueprints
    from routes.upload import upload_bp
    from routes.summarize import summarize_bp
    from routes.classify import classify_bp
    from routes.translate import translate_bp
    from routes.ocr import ocr_bp
    from routes.status import status_bp
    from routes.rag import rag_bp

    app.register_blueprint(upload_bp)
    app.register_blueprint(summarize_bp)
    app.register_blueprint(classify_bp)
    app.register_blueprint(translate_bp)
    app.register_blueprint(ocr_bp)
    app.register_blueprint(status_bp)
    app.register_blueprint(rag_bp)


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
