from fastapi import FastAPI
# from config.database import setup_database
from src.blog.endpoints import router as blog_endpoints

app = FastAPI()

# setup_database(app)

app.include_router(blog_endpoints)
# app.include_router(units_endpoints)