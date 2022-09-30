from fastapi import FastAPI

from v1.user.student import student
from v1.user import user
from models import models
from db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(student.router)
