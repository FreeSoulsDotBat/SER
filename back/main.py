from fastapi import FastAPI
from v1.users import router
from models import models
from db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
