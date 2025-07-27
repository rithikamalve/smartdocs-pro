import requests
import os

def test_status():
    resp = requests.get('http://localhost:5000/status')
    assert resp.status_code == 200
    assert resp.json()['status'] == 'ok'

