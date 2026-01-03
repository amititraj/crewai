from pydantic import BaseModel, Field
from typing import Optional, List
from .activity import Activity

class DayPlan(BaseModel):
    date: str
    summary: str
    activities: List[Activity]