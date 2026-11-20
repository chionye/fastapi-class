import os
import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from fs.core.config import UPLOAD_DIR, BASE_URL, MAX_FILE_SIZE, ALLOWED_EXTENSIONS
from fs.models.file import File

class FileValidationError(Exception):
    pass

def save_file(db: Session, upload: UploadFile, user_id: int):
    ext = os.path.splitext(upload.filename or "")[1];
    if ext not in ALLOWED_EXTENSIONS:
        raise FileValidationError(f"File type '{ext}' not allowed'")

    stored_name = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join(UPLOAD_DIR, stored_name)

    size = 0