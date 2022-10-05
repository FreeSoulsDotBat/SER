from pydoc import synopsis
from pyexpat import model
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from schemas import schemas
from models import models


router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/book/book_class", status_code=201)
async def create_book_class(book_class: schemas.BookClassCreate, db: Session = Depends(get_db)):

    db_book_class = models.BookClass(
        id_book=book_class.id_book, id_class=book_class.id_class)

    db.add(db_book_class)
    db.commit()

    return {"status": 201}


@router.get("/book/book_class/{book_id}", response_model=schemas.BookClass)
async def get_book_class_by_id(book_class_id: int, db: Session = Depends(get_db)):
    return db.query(models.BookClass).get(book_class_id)


@router.put("/book/book_class/{book_id}", status_code=200)
async def update_book_class(book_class_id: int, changes: schemas.BookClassUpdate, db: Session = Depends(get_db)):
    db_book_class = db.get(models.BookClass, book_class_id)

    if not db_book_class:
        raise HTTPException(status_code=404, detail="Book Class not found")
    to_change = changes.dict(exclude_unset=True)

    for key, value in to_change.items():
        setattr(db_book_class, key, value)

    db.add(db_book_class)
    db.commit()

    return {"status": 200}


@router.delete("/book/book_class/{book_id}", status_code=204)
async def delete_book_class(book_class_id: int, db: Session = Depends(get_db)):
    db_book_class = db.get(models.BookClass, book_class_id)

    if not db_book_class:
        raise HTTPException(status_code=404, detail="Book Class not found")

    db.delete(db_book_class)
    db.commit()

    return {"status": 204}
