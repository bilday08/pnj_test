from dotenv import load_dotenv
import os

load_dotenv()

SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH")
API_URL = os.getenv("API_URL")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")
