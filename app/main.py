from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AssignmentRequest(BaseModel):
    course: str
    topic: str
    difficulty: str
    number_of_questions: int
    total_marks: int


@app.get("/")
def home():
    return {"message": "InstructorAI is running!"}


@app.post("/assignments")
def create_assignment(request: AssignmentRequest):
    return {
        "message": "Assignment request received",
        "course": request.course,
        "topic": request.topic,
        "difficulty": request.difficulty,
        "number_of_questions": request.number_of_questions,
        "total_marks": request.total_marks
    }