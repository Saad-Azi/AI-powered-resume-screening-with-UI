from crewai import Agent, Crew, Process, Task
from textwrap import dedent
from typing import Dict, List
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import os
from .tasks.resume_tasks import ResumeScreeningTasks
from .agents.resume_agents import ResumeScreeningAgents

# Load environment variables from a .env file
load_dotenv()

# Initialize the OpenAI language model
llm = ChatOpenAI(model="gpt-4")

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

class ResumeScreeningCrew:
    def __init__(self):
        self.agents = ResumeScreeningAgents()
        self.tasks = ResumeScreeningTasks()

    def create_crew(self, resume_path: str, job_criteria: Dict[str, any] = None):
        # Create tasks
        extraction_task = self.tasks.extraction_task(resume_path)
        analysis_task = self.tasks.analysis_task(job_criteria, [extraction_task])
        scoring_task = self.tasks.scoring_task([extraction_task, analysis_task])

        # Create and return the crew
        return Crew(
            agents=[
                self.agents.extractor_agent(),
                self.agents.analyzer_agent(),
                self.agents.scorer_agent()
            ],
            tasks=[extraction_task, analysis_task, scoring_task],
            process=Process.sequential,
            verbose=True
        )

# if __name__ == "__main__":
#     # Example job criteria
#     job_criteria = {
#         "title": "Software Engineer",
#         "min_experience": 2,
#         "required_skills": ["Python", "React", "Node.js"],
#         "level": "Mid"
#     }
    
#     try:
#         # Create and run the crew
#         resume_screening = ResumeScreeningCrew()
#         crew = resume_screening.create_crew(
#             resume_path="./resume.pdf",  # Make sure this path is correct
#             job_criteria=job_criteria
#         )
        
#         result = crew.kickoff()
#         print(result)
#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
