from fastapi import FastAPI
from pydantic import BaseModel
from db_setup import engine, users_table

app = FastAPI()

class UserIn(BaseModel):
    name: str

@app.post("/api/submit")
async def submit(user: UserIn):
    with engine.begin() as conn:
        conn.execute(users_table.insert().values(name=user.name))
    return {"message": "User submitted"}
