from typing import Union, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from .models import Student as ModelStudent
from .schema import StudentWrite, Student as SchemaStudent

import os

postgres_socket_dir = os.path.join(os.environ["DEVENV_STATE"], "postgres")
dev_sqlalchemy_url = f"postgresql+psycopg2://postgres:postgres@/backend?host={postgres_socket_dir}"

origins = [
    "http://localhost:3000",
]

app = FastAPI(docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(DBSessionMiddleware, db_url=dev_sqlalchemy_url)

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

@app.post("/students", response_model=SchemaStudent)
def create_student(user: StudentWrite):
    db_student = ModelStudent(
        name=user.name,
        surname=user.surname,
        age=user.age,
        email=user.email
    )
    db.session.add(db_student)
    db.session.commit()
    db.session.refresh(db_student)
    return db_student

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


def start():
    """Launched with `poetry run start` at root level"""
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
