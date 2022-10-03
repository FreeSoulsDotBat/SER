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


@router.post("/user/student/", status_code=201)
async def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):

    db_student = models.Student(id_user=student.id_user,
                                id_classroom=student.id_classroom,
                                id_class=student.id_class)
    db.add(db_student)
    db.commit()

    return {"status": 201}


@router.get("/user/student/{student_id}", response_model=schemas.Student)
async def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Student).get(student_id)


@router.put("/user/student/{student_id}", status_code=200)
async def update_student(student_id: int, changes: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.get(models.Student, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    to_change = changes.dict(exclude_unset=True)
    for key, value in to_change.items():
        setattr(db_student, key, value)

    db.add(db_student)
    db.commit()

    return {"status": 200}


@router.delete("/user/{student_id}", status_code=204)
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.get(models.Student, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()

    return {"status": 204}
