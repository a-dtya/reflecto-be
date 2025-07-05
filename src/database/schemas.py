#defines api input/ output format
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkEntryCreate(BaseModel):
    entry: str

class WorkEntryResponse(BaseModel):
    id: int
    user_id: str
    entry: str
    polished_output: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
        