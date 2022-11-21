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


@router.post("/notification/", status_code=201)
async def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):

    db_notification = models.Notification(message=notification.message,
                                          recurrent=notification.recurrent,
                                          notification_date=notification.notification_date,
                                          link=notification.link,
                                          photo=notification.photo,
                                          notification_week_day=notification.notification_week_day)

    db.add(db_notification)
    db.commit()

    return {"status": 201}


@router.get("/notification/{notification_id}", response_model=schemas.Notification)
async def get_notification_by_id(notification_id: int, db: Session = Depends(get_db)):
    return db.query(models.Notification).get(notification_id)


@router.put("/notification/{notification_id}", status_code=200)
async def update_notification(notification_id: int, changes: schemas.NotificationUpdate, db: Session = Depends(get_db)):
    db_notification = db.get(models.Notification, notification_id)

    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    to_change = changes.dict(exclude_unset=True)
    for key, value in to_change.items():
        setattr(db_notification, key, value)

    db.add(db_notification)
    db.commit()

    return {"status": 200}


@router.delete("/notification/{notification_id}", status_code=204)
async def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = db.get(models.Notification, notification_id)

    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    db.delete(db_notification)
    db.commit()

    return {"status": 204}
