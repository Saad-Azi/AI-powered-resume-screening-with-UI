from pydantic import BaseModel
from typing import Optional

class ScreeningResponse(BaseModel):
    status: str
    result: str
    error: Optional[str] = None 