from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AssignmentRequest(BaseModel):
    course: str
    topic: str
    difficulty: str
    number_of_questions: int
    total_marks: int


class RubricItem(BaseModel):
    criterion: str
    description: str
    marks: int


class Question(BaseModel):
    question: str
    marks: int


class Assignment(BaseModel):
    title: str
    course: str
    topic: str
    difficulty: str
    questions: list[Question]
    rubric: list[RubricItem]
    total_marks: int
    suggested_deadline: str


@app.get("/")
def home():
    return {"message": "InstructorAI is running!"}


@app.post("/assignments", response_model=Assignment)
def create_assignment(request: AssignmentRequest):

    questions = []

    for i in range(request.number_of_questions):
        question = Question(
            question=f"Sample question {i + 1} about {request.topic}",
            marks=request.total_marks // request.number_of_questions
        )

        questions.append(question)

    rubric = [
        RubricItem(
            criterion="Correctness",
            description="The solution produces the correct result.",
            marks=8
        ),
        RubricItem(
            criterion="Logic",
            description="The solution uses appropriate programming logic.",
            marks=6
        ),
        RubricItem(
            criterion="Code Quality",
            description="The code is clear, readable, and properly structured.",
            marks=6
        )
    ]

    assignment = Assignment(
        title=f"{request.course} - {request.topic}",
        course=request.course,
        topic=request.topic,
        difficulty=request.difficulty,
        questions=questions,
        rubric=rubric,
        total_marks=request.total_marks,
        suggested_deadline="2026-10-05"
    )

    return assignment