from crewai import Task
from textwrap import dedent
from typing import Dict, List
from ..services.resume_parser import ResumeParser
from ..agents.resume_agents import ResumeScreeningAgents

class ResumeScreeningTasks:
    def __init__(self):
        self.agents = ResumeScreeningAgents()
        self.parser = ResumeParser()

    def extraction_task(self, resume_path: str):
        resume_text = self.parser.extract_text_from_pdf(resume_path)
        return Task(
            description=dedent(f"""
                Extract key information from the following resume text:
                
                {resume_text}

                Focus on:
                1. Skills and technologies
                2. Work experience and duration
                3. Educational background
                4. Professional certifications
                
                Provide the information in a structured format as a dictionary with the following keys:
                - skills: [list of skills]
                - experience: [list of dict containing company, role, duration, responsibilities]
                - education: [list of dict containing degree, institution, year]
                - certifications: [list of certifications]
            """),
            expected_output="Dictionary containing extracted resume information",
            agent=self.agents.extractor_agent()
        )

    def analysis_task(self, job_criteria: Dict, context: List[Task]):
        return Task(
            description=dedent(f"""
                Analyze the extracted resume information against the following criteria:
                {job_criteria if job_criteria else 'Standard evaluation criteria'}
                
                Evaluate:
                1. Skills match and relevance
                2. Experience quality and quantity
                3. Education relevance
                4. Overall profile strength
            """),
            expected_output="Detailed analysis report of the candidate's qualifications",
            agent=self.agents.analyzer_agent(),
            context=context
        )

    def scoring_task(self, context: List[Task]):
        return Task(
            description=dedent("""
                Based on the analysis:
                1. Generate an overall score (0-100)
                2. Provide scoring breakdown by category
                3. Add specific recommendations
            """),
            expected_output="Final score report with detailed breakdown and recommendations",
            agent=self.agents.scorer_agent(),
            context=context
        ) 