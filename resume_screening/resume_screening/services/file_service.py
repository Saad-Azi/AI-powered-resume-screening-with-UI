import os
import shutil
from datetime import datetime
from fastapi import UploadFile

class FileService:
    def __init__(self, upload_dir: str):
        self.upload_dir = upload_dir

    async def save_upload(self, file: UploadFile) -> str:
        """Save uploaded file and return the path"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"resume_{timestamp}.pdf"
        file_path = os.path.join(self.upload_dir, filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return file_path

    @staticmethod
    def cleanup_file(file_path: str):
        """Remove file if it exists"""
        if os.path.exists(file_path):
            os.remove(file_path) 