from crewai import Agent
from textwrap import dedent
from ..config import llm

class ResumeScreeningAgents:
    @staticmethod
    def extractor_agent():
        return Agent(
            role="Resume Information Extractor",
            goal="Extract key information from resumes accurately",
            backstory=dedent("""
                You are an expert at parsing resumes and extracting structured information 
                from various document formats. You have extensive experience in identifying 
                and categorizing professional details.
            """),
            llm=llm,
            verbose=True
        )

    @staticmethod
    def analyzer_agent():
        return Agent(
            role="Resume Analyzer",
            goal="Analyze extracted resume information and provide detailed evaluation",
            backstory=dedent("""
                You are an experienced HR professional with expertise in evaluating 
                candidate qualifications and matching them to job requirements. 
                You excel at objective assessment and scoring.
            """),
            llm=llm,
            verbose=True
        )

    @staticmethod
    def scorer_agent():
        return Agent(
            role="Resume Scorer",
            goal="Generate final scores and recommendations based on analysis",
            backstory=dedent("""
                You are a hiring specialist who excels at quantifying candidate 
                qualifications and providing clear, actionable insights for hiring decisions.
            """),
            llm=llm,
            verbose=True
        ) 