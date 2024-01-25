from pydantic import BaseModel

class StudentSchema(BaseModel):
    first_name: str
    last_name: str
    age: int
    gpa: float
