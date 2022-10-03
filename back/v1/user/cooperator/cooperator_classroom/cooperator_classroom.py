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


@router.post("/user/cooperator/cooperator_classroom/", status_code=201)
async def create_cooperator_classroom(cooperator_classroom: schemas.CooperatorClassroomCreate, db: Session = Depends(get_db)):

    db_cooperator_classroom = models.CooperatorClassroom(id_classroom=cooperator_classroom.id_classroom,
                                                         id_cooperator=cooperator_classroom.id_cooperator)

    db.add(db_cooperator_classroom)
    db.commit()

    return {"status": 201}


@router.get("/user/cooperator/cooperator_classroom/{cooperator_classroom_id}", response_model=schemas.CooperatorClassroom)
async def get_cooperator_classroom_by_id(cooperator_classroom_id: int, db: Session = Depends(get_db)):
    return db.query(models.CooperatorClassroom).get(cooperator_classroom_id)


@router.put("/user/cooperator/cooperator_classroom/{cooperator_classroom_id}", status_code=200)
async def update_cooperator_classroom(cooperator_classroom_id: int, changes: schemas.CooperatorClassroomUpdate, db: Session = Depends(get_db)):
    db_cooperator_classroom = db.get(
        models.CooperatorClassroom, cooperator_classroom_id)

    if not db_cooperator_classroom:
        raise HTTPException(
            status_code=404, detail="Cooperator Class Room not found")
    to_change = changes.dict(exclude_unset=True)
    for key, value in to_change.items():
        setattr(db_cooperator_classroom, key, value)

    db.add(db_cooperator_classroom)
    db.commit()

    return {"status": 200}


@router.delete("/user/cooperator/cooperator_classroom/{cooperator_classroom_id}", status_code=204)
async def delete_cooperator_classroom(cooperator_classroom_id: int, db: Session = Depends(get_db)):
    db_cooperator_classroom = db.get(
        models.CooperatorClassroom, cooperator_classroom_id)
    if not db_cooperator_classroom:
        raise HTTPException(
            status_code=404, detail="Cooperator Class Room not found")

    db.delete(db_cooperator_classroom)
    db.commit()

    return {"status": 204}
