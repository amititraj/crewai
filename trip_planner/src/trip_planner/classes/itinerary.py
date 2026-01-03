from pydantic import BaseModel, Field
from typing import Optional, List
from .dayplan import DayPlan

class Itinerary(BaseModel):
    destination: str
    start_date: str
    end_date: str
    total_days: int
    theme: List[str] = Field(default_factory=list)
    budget_note: Optional[str] = None
    daily_plan: List[DayPlan]
    packing_tips: List[str] = Field(default_factory=list)
    local_basics: List[str] = Field(default_factory=list)