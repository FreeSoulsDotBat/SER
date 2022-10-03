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


@router.post("/user/cooperator/", status_code=201)
async def create_cooperator(cooperator: schemas.CooperatorCreate, db: Session = Depends(get_db)):

    db_cooperator = models.Cooperator(id_user=cooperator.id_user)

    db.add(db_cooperator)
    db.commit()

    return {"status": 201}


@router.get("/user/cooperator/{cooperator_id}", response_model=schemas.Cooperator)
async def get_cooperator_by_id(cooperator_id: int, db: Session = Depends(get_db)):
    return db.query(models.Cooperator).get(cooperator_id)


@router.put("/user/cooperator/{cooperator_id}", status_code=200)
async def update_cooperator(cooperator_id: int, changes: schemas.CooperatorUpdate, db: Session = Depends(get_db)):

    db_cooperator = db.get(models.Cooperator, cooperator_id)

    if not db_cooperator:
        raise HTTPException(status_code=404, detail="Cooperator not found")
    to_change = changes.dict(exclude_unset=True)
    for key, value in to_change.items():
        setattr(db_cooperator, key, value)

    db.add(db_cooperator)
    db.commit()

    return {"status": 200}


@router.delete("/user/cooperator/{cooperator_id}")
async def delete_cooperator(cooperator_id: int, db: Session = Depends(get_db)):

    db_cooperator = db.get(models.Cooperator, cooperator_id)
    if not db_cooperator:
        raise HTTPException(status_code=404, detail="Cooperator not found")

    db.delete(db_cooperator)
    db.commit()

    return {"status": 204}
