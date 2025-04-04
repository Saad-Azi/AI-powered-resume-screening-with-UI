from setuptools import setup, find_packages

setup(
    name="resume_screening",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "python-multipart",
        "crewai",
        "langchain-openai",
        "python-dotenv",
        "PyPDF2"
    ],
)
