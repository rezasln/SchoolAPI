from pymongo import MongoClient
from pymongo.collection import Collection
from models import StudentModel
from schemas import StudentSchema

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Connect to the 'school' database
db = client['school']

# Access the 'students' collection within the 'school' database
students_collection: Collection = db['students']

# Function to add a student to the database
def add_student(student: StudentSchema):
    return students_collection.insert_one(student.dict())

# Function to get all students from the database
def get_all_students():
    return list(students_collection.find())

# Function to get a student by name
def get_student_by_name(student_name):
    student = students_collection.find_one({"first_name": student_name})
    if student:
        student['id'] = str(student['_id'])
    return student

# Function to delete a student by ID
def delete_student(student_id):
    return students_collection.delete_one({"_id": student_id})
