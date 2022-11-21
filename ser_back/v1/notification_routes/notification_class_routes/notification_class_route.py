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


@router.post("/notification/notification_class/", status_code=201)
async def create_notification_class(notification_class: schemas.NotificationClassCreate, db: Session = Depends(get_db)):

    db_notification_class = models.NotificationClass(id_notification=notification_class.id_notification,
                                                     id_class=notification_class.id_class)

    db.add(db_notification_class)
    db.commit()

    return {"status": 201}


@router.get("/notification/notification_class/{notification_class_id}", response_model=schemas.NotificationClass)
async def get_notification_class_by_id(notification_class_id: int, db: Session = Depends(get_db)):
    return db.query(models.NotificationClass).get(notification_class_id)


@router.put("/notification/notification_class/{notification_class_id}", status_code=200)
async def update_notification_class(notification_class_id: int, changes: schemas.NotificationClassUpdate, db: Session = Depends(get_db)):

    db_notification_class = db.get(
        models.NotificationClass, notification_class_id)

    if not db_notification_class:
        raise HTTPException(
            status_code=404, detail="Notification Class not found")
    to_change = changes.dict(exclude_unset=True)

    for key, value in to_change.items():
        setattr(db_notification_class, key, value)

    db.add(db_notification_class)
    db.commit()

    return {"status": 200}


@router.delete("/notification/notification_class/{notification_class_id}", status_code=204)
async def delete_notification_class(notification_class_id: int, db: Session = Depends(get_db)):
    db_notification_class = db.get(
        models.NotificationClass, notification_class_id)

    db.delete(db_notification_class)
    db.commit()

    return {"status": 204}
