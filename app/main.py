from fastapi import FastAPI
from back.models.models import Base
from back.db.database import SessionLocal, engine
from routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
