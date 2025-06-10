import requests
from config import settings

def extract_from_api():
    response = requests.get(settings.API_URL)
    response.raise_for_status()
    return response.json()