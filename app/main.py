from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.services.countries import get_countries
from app.controllers.controller import router


initials = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    initials["country_code"] = get_countries()
    yield
    initials.clear()


app = FastAPI(
    title='Countries REST API',
    contact={
        "name": "Joshua Lartey",
        "url": "https://www.linkedin.com/in/joshua-lartey-2ba404199/",
        "email": "larteyjoshua@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    lifespan=lifespan

)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "Hello World"}

app.include_router(router)
