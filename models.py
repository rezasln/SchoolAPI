from pydantic import BaseModel

class StudentModel(BaseModel):
    id: str  
    first_name: str
    last_name: str
    age: int
    gpa: float
