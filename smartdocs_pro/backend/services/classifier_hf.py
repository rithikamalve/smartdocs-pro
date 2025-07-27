import requests
from config import load_config

HF_API_URL = "https://api-inference.huggingface.co/models/joeddav/xlm-roberta-large-xnli"
HF_API_KEY = load_config().get('HF_API_KEY')

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def classify(text):
    payload = {"inputs": text}
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"HF Classification failed: {response.text}") 