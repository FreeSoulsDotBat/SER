from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from models.models import User
# from main import get_db
# from schemas.schemas import User, UserCreate

router = APIRouter()


# @router.post("/user/", response_model=User)
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(email=user.email,
#                    password=user.password,
#                    first_name=user.first_name,
#                    last_name=user.last_name,
#                    birthday=user.birthday,
#                    supervision=user.supervision,
#                    supervision_area=user.supervision_area,
#                    phone=user.phone,
#                    photo=user.photo)

#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


@router.get("/user/{id}")
async def get_user_by_id(id):
    return {"id": "test"}
