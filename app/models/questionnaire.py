from pydantic import BaseModel
from typing import List, Optional

class QuestionOption(BaseModel):
    label: str
    value: str
    score: float

class Question(BaseModel):
    id: str
    layer: str
    layer_index: int
    dimension: str
    text: str
    type: str
    options: Optional[List[QuestionOption]] = None
    data_purpose: str

class Answer(BaseModel):
    question_id: str
    value: str
