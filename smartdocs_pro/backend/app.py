from flask import Flask
from flask_cors import CORS
from config import load_config

def create_app():
    app = Flask(__name__)
    CORS(app)
    load_config(app)
    print("Flask app is initializing...")

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

    @app.route("/", methods=["GET"])
    def health():
        return {"status": "ok"}, 200

    return app
