from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from route.route_barang import barang
from route.route_user import user
from database import engine
from sqlmodel import SQLModel
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()


UPLOAD_FOLDER = "route/uploaded_images"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.mount("/uploaded_images", StaticFiles(directory=UPLOAD_FOLDER), name="uploaded_images")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user , prefix = '/user' , tags=['User'])
app.include_router(barang, prefix='/barang', tags=['Barang'])  