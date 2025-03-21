from PyPDF2 import PdfReader
import os

class ResumeParser:
    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> str:
        """Extract text content from a PDF file."""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Resume file not found at: {pdf_path}")
        
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}") 