from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db_models import Question as DBQuestion
# from schemas import QuestionCreate
from typing import List
import requests
import json


async def get_question(db: AsyncSession) -> DBQuestion:
    query = (
        select(DBQuestion)
        .order_by(DBQuestion.created_at.desc())
    )
    result = await db.execute(query)
    return result.scalars().first() if result else None 


async def add_question(db: AsyncSession, number: int):
    url = f'https://jservice.io/api/random?count={number}'
    print(url)
    response = requests.get(url)
    list_of_questions = json.loads(response.content)
    #ids = await get_ids(db)
    for q in list_of_questions:    
        ids = await get_ids(db)
        id = q['id']
        while id in ids:
            await get_one_question()
        else:
            db_question = DBQuestion(
                id = q['id'],
                question_text = q['question'],
                answer_text = q['answer']
            )
            db.add(db_question)
            await db.commit()
            await db.refresh(db_question)
            

async def get_ids(db: AsyncSession) -> List[int]:
    result = await db.execute(select(DBQuestion.id))
    return result.scalars().all()


async def get_one_question():
    response = requests.get('https://jservice.io/api/random?count=1')
    question = json.loads(response.content)[0]
    return question


    

