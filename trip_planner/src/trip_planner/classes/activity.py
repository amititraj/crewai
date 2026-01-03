from pydantic import BaseModel, Field
from typing import Optional, List

class Activity(BaseModel):
    time: str = Field(description="Estimated time slot, e.g., '08:00–9:30'")
    title: str
    details: str
    booking_link: Optional[str] = None