from app import create_app
import logging

try:
    app = create_app()
except Exception as e:
    logging.exception("WSGI app failed to create")
    raise
