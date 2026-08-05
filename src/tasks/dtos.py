from pydantic import BaseModel

class TaskCreateDTO(BaseModel):
    title: str
    description: str
    is_completed: bool = False