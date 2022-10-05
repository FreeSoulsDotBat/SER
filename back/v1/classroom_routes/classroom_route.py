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


@router.post("/classroom/", status_code=201)
async def create_classroom(classroom_body: schemas.ClassroomCreate, db: Session = Depends(get_db)):

    db_classroom = models.Classroom(floor=classroom_body.floor,
                                    classroom_number=classroom_body.classroom_number,
                                    number_students=classroom_body.number_students,
                                    photo=classroom_body.photo,
                                    last_class_day=classroom_body.last_class_day,
                                    next_class_day=classroom_body.next_class_day,
                                    id_class=classroom_body.id_class)

    db.add(db_classroom)
    db.commit()

    return {"status": 201}


@router.get("/classroom/{classroom_id}", response_model=schemas.Classroom)
async def get_classroom_by_id(classroom_id: int, db: Session = Depends(get_db)):
    return db.query(models.Classroom).get(classroom_id)


@router.put("/classroom/{classroom_id}", status_code=200)
async def update_classroom_by_id(classroom_id: int, changes: schemas.ClassroomUpdate, db: Session = Depends(get_db)):
    db_classroom = db.get(models.Classroom, classroom_id)

    if not db_classroom:
        raise HTTPException(
            status_code=404, detail="Classroom not found")
    to_change = changes.dict(exclude_unset=True)
    for key, value in to_change.items():
        setattr(db_classroom, key, value)

    db.add(db_classroom)
    db.commit()

    return {"status": 200}


@router.delete("/classroom/{classroom_id}")
async def delete_classroom(classroom_id: int, db: Session = Depends(get_db)):
    db_classroom = db.get(models.Classroom, classroom_id)

    if not db_classroom:
        raise HTTPException(
            status_code=404, detail="Classroom not found")

    db.delete(db_classroom)
    db.commit()

    return {"status": 204}
