from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from schemas import QuestionAdd
import crud
from typing import Optional

router = APIRouter()


@router.post("/question", response_model=Optional[QuestionAdd])
async def create_question(number: int, db: AsyncSession = Depends(get_async_session)):
    question = await crud.get_question(db)
    await crud.add_question(db, number)
    return question