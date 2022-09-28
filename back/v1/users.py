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


@router.post("/user/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = models.User(email=user.email,
                          password=user.password,
                          first_name=user.first_name,
                          last_name=user.last_name,
                          birthday=user.birthday,
                          supervision=user.supervision,
                          supervision_area=user.supervision_area,
                          phone=user.phone,
                          photo=user.photo)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"status": 201}


@router.get("/user/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.User).get(user_id)


@router.put("/user/{user_id}")
async def update_user(user_id: int, changes: schemas.UserUpdate, db: Session = Depends(get_db)):

    db_user = db.get(models.User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    to_change = changes.dict(exclude_unset=True)
    for key, value in to_change.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.delete("/user/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(models.User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"status": 204}
