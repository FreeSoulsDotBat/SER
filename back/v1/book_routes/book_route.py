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


@router.post("/book/", status_code=201)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):

    db_book = models.Book(book_name=book.book_name,
                          actual_chapter=book.actual_chapter,
                          synopsis=book.synopsis,
                          beginning_date=book.beginning_date,
                          end_date=book.end_date)

    db.add(db_book)
    db.commit()

    return {"status": 201}


@router.get("/book/{book_id}", response_model=schemas.Book)
async def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).get(book_id)


@router.put("/book/{book_id}", status_code=200)
async def update_book(book_id: int, changes: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.get(models.Book, book_id)

    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    to_change = changes.dict(exclude_unset=True)

    for key, value in to_change.items():
        setattr(db_book, key, value)

    db.add(db_book)
    db.commit()

    return {"status": 200}


@router.delete("/book/{book_id}", status_code=204)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.get(models.Book, book_id)

    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(db_book)
    db.commit()

    return {"status": 204}
