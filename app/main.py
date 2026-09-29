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
    rubric: list[RubricItem]


class Assignment(BaseModel):
    title: str
    course: str
    topic: str
    difficulty: str
    questions: list[Question]
    total_marks: int
    suggested_deadline: str


@app.get("/")
def home():
    return {"message": "InstructorAI is running!"}


@app.post("/assignments", response_model=Assignment)
def create_assignment(request: AssignmentRequest):

    questions = []

    question_marks = request.total_marks // request.number_of_questions

    for i in range(request.number_of_questions):

        rubric = [
            RubricItem(
                criterion="Correctness",
                description="The solution produces the correct result.",
                marks=2
            ),
            RubricItem(
                criterion="Logic",
                description="The solution uses appropriate programming logic.",
                marks=1
            ),
            RubricItem(
                criterion="Code Quality",
                description="The code is clear, readable, and properly structured.",
                marks=1
            )
        ]

        question = Question(
            question=f"Sample question {i + 1} about {request.topic}",
            marks=question_marks,
            rubric=rubric
        )

        questions.append(question)

    assignment = Assignment(
        title=f"{request.course} - {request.topic}",
        course=request.course,
        topic=request.topic,
        difficulty=request.difficulty,
        questions=questions,
        total_marks=request.total_marks,
        suggested_deadline="2026-10-05"
    )

    return assignment