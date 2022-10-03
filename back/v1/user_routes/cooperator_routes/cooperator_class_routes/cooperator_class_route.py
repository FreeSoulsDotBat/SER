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


@router.post("/user/cooperator/cooperator_class/", status_code=201)
async def create_cooperator_class(cooperator_class: schemas.CooperatorClassCreate, db: Session = Depends(get_db)):

    db_cooperator_class = models.CooperatorClass(id_class=cooperator_class.id_class,
                                                 id_cooperator=cooperator_class.id_cooperator)

    db.add(db_cooperator_class)
    db.commit()

    return {"status": 201}


@router.get("/user/cooperator/cooperator_class/{cooperator_class_id}", response_model=schemas.CooperatorClass)
async def get_cooperator_class_by_id(cooperator_class_id: int, db: Session = Depends(get_db)):
    return db.query(models.CooperatorClass).get(cooperator_class_id)


@router.put("/user/cooperator/cooperator_class/{cooperator_class_id}", status_code=200)
async def update_cooperator_class(cooperator_class_id: int, changes: schemas.CooperatorClassUpdate, db: Session = Depends(get_db)):
    db_cooperator_class = db.get(models.CooperatorClass, cooperator_class_id)

    if not db_cooperator_class:
        raise HTTPException(
            status_code=404, detail="Cooperator Class not found")
    to_change = changes.dict(exclude_unset=True)
    for key, value in to_change.items():
        setattr(db_cooperator_class, key, value)

    db.add(db_cooperator_class)
    db.commit()

    return {"status": 200}


@router.delete("/user/cooperator/cooperator_class/{cooperator_class_id}", status_code=204)
async def delete_cooperator_class(cooperator_class_id: int, db: Session = Depends(get_db)):
    db_cooperator_class = db.get(models.CooperatorClass, cooperator_class_id)
    if not db_cooperator_class:
        raise HTTPException(
            status_code=404, detail="Cooperator Class not found")

    db.delete(db_cooperator_class)
    db.commit()

    return {"status": 204}
