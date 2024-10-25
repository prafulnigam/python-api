from fastapi import FastAPI
from app.routes import blog_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Blog API"}

app.include_router(blog_router, prefix="/blogs", tags=["blogs"])
