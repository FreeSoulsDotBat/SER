from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas import schemas
from models import models

router = APIRouter()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
