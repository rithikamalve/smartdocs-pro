import requests
import streamlit as st
import os
API_URL = st.secrets["API_URL"]

def upload_file(file):
    files = {'file': (file.name, file, file.type)}
    resp = requests.post(f'{API_URL}/upload', files=files)
    return resp.json()

def summarize_doc(doc_id, ext):
    resp = requests.post(f'{API_URL}/summarize', json={'document_id': doc_id, 'ext': ext})
    return resp.json()

def classify_doc(doc_id, ext):
    resp = requests.post(f'{API_URL}/classify', json={'document_id': doc_id, 'ext': ext})
    return resp.json()

def translate_doc(doc_id, ext, target_lang):
    resp = requests.post(f'{API_URL}/translate', json={'document_id': doc_id, 'ext': ext, 'target_lang': target_lang})
    return resp.json()

def ocr_doc(doc_id, ext):
    resp = requests.post(f'{API_URL}/ocr', json={'document_id': doc_id, 'ext': ext})
    return resp.json()

def rag_qa(doc_id, ext, question):
    data = {
        'document_id': doc_id,
        'ext': ext,
        'question': question
    }
    resp = requests.post(f'{API_URL}/rag', json=data)
    print("RAW RESPONSE:", resp.text)
    resp.raise_for_status() 
    return resp.json()


