from fastapi import FastAPI
from router import router
import datetime as dt
app = FastAPI(title="Text Analyzer API", version="1.0.0")
app.include_router(router)


@app.get("/")
def root(date):

    return {
        "message": "Добро пожаловать в Text Analyzer API",
        "docs": "/docs",
    }
