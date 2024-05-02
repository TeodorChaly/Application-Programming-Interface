from pydantic import BaseModel
from typing import Optional


class STaskAdded(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdded):
    id: int
