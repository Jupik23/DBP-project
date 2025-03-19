from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, database
from database import engine, get_db
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}