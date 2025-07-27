import os
from dotenv import load_dotenv

def load_config(app=None):
    load_dotenv()
    config = {
        'GROQ_API_KEY': os.getenv('GROQ_API_KEY'),
        'HF_API_KEY': os.getenv('HF_API_KEY'),
        # Database is always smartdocs.db in project root
        'DB_PATH': 'smartdocs.db',
    }
    if app:
        app.config.update(config)
    return config 