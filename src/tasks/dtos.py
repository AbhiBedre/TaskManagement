from pydantic import BaseModel

class TaskCreateDTO(BaseModel):
    title: str
    description: str
    is_completed: bool = False

class TaskResponseDTO(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool = False