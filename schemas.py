from pydantic import BaseModel
import datetime
from typing import Optional

# class QuestionCreate(BaseModel):
#     questions_num: int

#     class Config:
#         from_attributes = True


class QuestionAdd(BaseModel):
    id: int
    question_text: str
    answer_text: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True
