from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from v1.user_routes.student_routes import student_route
from v1.user_routes.cooperator_routes import cooperator_route
from v1.user_routes.cooperator_routes.cooperator_class_routes import cooperator_class_route
from v1.user_routes.cooperator_routes.cooperator_classroom_routes import cooperator_classroom_route
from v1.class_routes import class_route
from v1.classroom_routes import classroom_route
from v1.user_routes import user_route
from models import models
from db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_route.router)
app.include_router(student_route.router)
app.include_router(cooperator_route.router)
app.include_router(cooperator_class_route.router)
app.include_router(cooperator_classroom_route.router)
app.include_router(class_route.router)
app.include_router(classroom_route.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SER",
        version="0.1",
        description="Rest API of SER",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
