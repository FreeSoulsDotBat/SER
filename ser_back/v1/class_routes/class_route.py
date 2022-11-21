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


@router.post("/class/", status_code=201)
async def create_class(class_body: schemas.ClassCreate, db: Session = Depends(get_db)):

    db_class = models.Class(beginning_date=class_body.beginning_date,
                            semester=class_body.semester,
                            number_students=class_body.number_students,
                            number_cooperators=class_body.number_cooperators,
                            number_classrooms=class_body.number_classrooms)

    db.add(db_class)
    db.commit()

    return {"status": 201}


@router.get("/class/{class_id}", response_model=schemas.Class)
async def get_class_by_id(class_id: int, db: Session = Depends(get_db)):
    return db.query(models.Class).get(class_id)


@router.put("/class/{class_id}", status_code=200)
async def update_class_by_id(class_id: int, changes: schemas.ClassUpdate, db: Session = Depends(get_db)):
    db_class = db.get(models.Class, class_id)

    if not db_class:
        raise HTTPException(
            status_code=404, detail="Class not found")
    to_change = changes.dict(exclude_unset=True)
    for key, value in to_change.items():
        setattr(db_class, key, value)

    db.add(db_class)
    db.commit()

    return {"status": 200}


@router.delete("/class/{class_id}")
async def delete_class(class_id: int, db: Session = Depends(get_db)):
    db_class = db.get(models.Class, class_id)

    if not db_class:
        raise HTTPException(
            status_code=404, detail="Class not found")

    db.delete(db_class)
    db.commit()

    return {"status": 204}
