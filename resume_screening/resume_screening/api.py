from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
from .config import UPLOAD_DIR
from .models.request_models import JobCriteria
from .models.response_models import ScreeningResponse
from .services.file_service import FileService
from .main import ResumeScreeningCrew

app = FastAPI(
    title="Resume Screening API",
    description="API for screening resumes against job descriptions",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

file_service = FileService(UPLOAD_DIR)

@app.post("/screen-resume/", response_model=ScreeningResponse)
async def screen_resume(
    resume: UploadFile = File(...),
    title: str = Form(...),
    min_experience: int = Form(...),
    required_skills: str = Form(...),
    level: str = Form(...)
):
    temp_path = None
    try:
        if not resume.filename.endswith('.pdf'):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported"
            )

        temp_path = await file_service.save_upload(resume)
        skills_list = [skill.strip() for skill in required_skills.split(',')]

        job_criteria = {
            "title": title,
            "min_experience": min_experience,
            "required_skills": skills_list,
            "level": level
        }

        resume_screening = ResumeScreeningCrew()
        crew = resume_screening.create_crew(
            resume_path=temp_path,
            job_criteria=job_criteria
        )
        
        result = crew.kickoff()
        
        return ScreeningResponse(
            status="success",
            result=str(result)
        )

    except Exception as e:
        return ScreeningResponse(
            status="error",
            result="",
            error=str(e)
        )
    finally:
        if temp_path:
            file_service.cleanup_file(temp_path)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Cleanup endpoint (optional, for maintenance)
@app.post("/cleanup-uploads")
async def cleanup_uploads():
    """Remove all files from the uploads directory"""
    try:
        for filename in os.listdir(UPLOAD_DIR):
            file_path = os.path.join(UPLOAD_DIR, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return {"status": "success", "message": "All uploaded files cleaned up"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
