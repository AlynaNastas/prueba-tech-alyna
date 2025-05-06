# project/src/api_client.py

import requests
import os

class ApiClient:
    def __init__(self):
        self.base_url = os.getenv('API_BASE_URL', 'https://api.example.com')

    def get_data(self, endpoint: str):
        response = requests.get(f"{self.base_url}/{endpoint}")
        response.raise_for_status()
        return response.json()

    def post_data(self, payload: dict):
        response = requests.post(f"{self.base_url}/submit", json=payload)
        response.raise_for_status()
        return response.json()
