import os

UPLOAD_DIR = "uploads"

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8889")

MAX_FILE_SIZE = 5 * 1024 * 1024

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".pdf"}

os.makedirs(UPLOAD_DIR, exist_ok=True)