import os
import requests
import json
from typing import Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
HEADERS = {'X-Api-Key': API_KEY}

class DataFetchError(Exception):
    pass

def fetch_data(url: str, name: str) -> list[dict[str, Any]]:
    """fetches animal data from API"""
    try:
        res = requests.get(url, params={'name': name}, headers=HEADERS)
        return res.json()
    except requests.exceptions.RequestException as e:
        raise DataFetchError(f"API request failed: {e}")

def load_data(file_path: str) -> list[dict[str, Any]]:
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)