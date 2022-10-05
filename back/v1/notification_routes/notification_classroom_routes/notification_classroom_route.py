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


@router.post("/notification/notification_classroom/", status_code=201)
async def create_notification_classroom(notification_classroom: schemas.NotificationClassroomCreate, db: Session = Depends(get_db)):

    db_notification_classroom = models.NotificationClassroom(id_notification=notification_classroom.id_notification,
                                                             id_classroom=notification_classroom.id_classroom)

    db.add(db_notification_classroom)
    db.commit()

    return {"status": 201}


@router.get("/notification/notification_classroom/{notification_classroom_id}", response_model=schemas.NotificationClassroom)
async def get_notification_classroom_by_id(notification_classroom_id: int, db: Session = Depends(get_db)):
    return db.query(models.NotificationClassroom).get(notification_classroom_id)


@router.put("/notification/notification_classroom/{notification_classroom_id}", status_code=200)
async def update_notification_classroom(notification_classroom_id: int, changes: schemas.NotificationClassroomUpdate, db: Session = Depends(get_db)):

    db_notification_classroom = db.get(
        models.NotificationClassroom, notification_classroom_id)

    if not db_notification_classroom:
        raise HTTPException(
            status_code=404, detail="Notification Classroom not found")
    to_change = changes.dict(exclude_unset=True)

    for key, value in to_change.items():
        setattr(db_notification_classroom, key, value)

    db.add(db_notification_classroom)
    db.commit()

    return {"status": 200}


@router.delete("/notification/notification_classroom/{notification_classroom_id}", status_code=204)
async def delete_notification_classroom(notification_classroom_id: int, db: Session = Depends(get_db)):
    db_notification_classroom = db.get(
        models.NotificationClassroom, notification_classroom_id)

    db.delete(db_notification_classroom)
    db.commit()

    return {"status": 204}
