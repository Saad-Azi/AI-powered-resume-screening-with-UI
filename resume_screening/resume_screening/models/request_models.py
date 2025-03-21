from pydantic import BaseModel
from typing import List

class JobCriteria(BaseModel):
    title: str
    min_experience: int
    required_skills: List[str]
    level: str 