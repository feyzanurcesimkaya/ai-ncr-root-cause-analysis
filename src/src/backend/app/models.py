from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Photo(BaseModel):
    url: str
    clarity_score: Optional[float] = None


class NCRBase(BaseModel):
    title: str
    description: str
    project: str
    location: str
    discipline: str
    severity: str = Field(..., regex="^(low|medium|high)$")


class NCRCreate(NCRBase):
    photos: list[Photo] = []


class NCR(NCRBase):
    id: int
    created_at: datetime
    status: str
    root_cause: Optional[str] = None

    class Config:
        orm_mode = True


class AISuggestion(BaseModel):
    defect_type: Optional[str] = None
    possible_root_cause: Optional[str] = None
    similar_case_ids: list[str] = []
