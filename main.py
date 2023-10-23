from fastapi import FastAPI
import api
from database import engine, Base


app = FastAPI(title="bw_test")

# @app.get("/")
# def hello():
#     return "hello world"

app.include_router(api.router)

@app.on_event("startup")
async def init_tables():
    # print(get_settings().db_url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
