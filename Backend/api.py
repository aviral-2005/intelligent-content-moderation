from fastapi import FastAPI
from routers.moderation import router as moderation_router
from fastapi.middleware.cors import CORSMiddleware
from exceptions.handlers import generic_exception_handler

app = FastAPI(
    title="Intelligent Content Review & Moderation API",
    version="1.0.0",
)

app.add_exception_handler(Exception, generic_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Content Moderation API is running!"}


app.include_router(moderation_router)
