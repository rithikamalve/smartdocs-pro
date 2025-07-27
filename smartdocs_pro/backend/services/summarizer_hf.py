import requests
from config import load_config

HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HF_API_KEY = load_config().get('HF_API_KEY')

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def summarize(text):
    payload = {"inputs": text}
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]['summary_text']
    else:
        raise Exception(f"HF Summarization failed: {response.text}") 