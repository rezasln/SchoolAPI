from fastapi import FastAPI, HTTPException
from database import add_student, get_all_students, get_student_by_name, delete_student
from models import StudentModel
from schemas import StudentSchema
from bson.objectid import ObjectId

app = FastAPI()

# Create a new student
@app.post("/students/", response_model=StudentModel, tags=["students"])
def create_student(student: StudentSchema):
    """
    Create a new student.
    """
    student_id = add_student(student)
    return {"id": str(student_id.inserted_id), **student.dict()}

# Retrieve all students
@app.get("/students/", response_model=list[StudentModel], tags=["students"])
def read_students():
    """
    Retrieve all students.
    Returns a list of all students present in the database.
    """
    students = get_all_students()
    
    # Add an 'id' field to each student dictionary in the list
    students_with_id = [{"id": str(student['_id']), **student} for student in students]
    
    return students_with_id

# Retrieve a specific student by name
@app.get("/students/{student_name}", response_model=StudentModel, tags=["students"])
def read_student(student_name: str):
    """
    Retrieve a specific student by name.
    """
    student = get_student_by_name(student_name)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

# Update a student by ID
@app.put("/students/{student_id}", response_model=StudentModel, tags=["students"])
def update_student(student_id: str, student: StudentSchema):
    """
    Update a student by ID.
    """
    # You can add update functionality here using the student_id
    # For now, let's just return the student as is
    return student

# Delete a student by ID
@app.delete("/students/{student_id}", response_model=dict, tags=["students"])
def delete_student_endpoint(student_id: str):
    """
    Delete a student by ID.
    """
    result = delete_student(ObjectId(student_id))
    if result.deleted_count == 1:
        return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
