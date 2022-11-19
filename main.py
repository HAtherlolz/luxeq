from fastapi import FastAPI
from config.database import setup_database
from src.blog.endpoints.categories_api import router as categories_endpoints
from src.blog.endpoints.articles_api import router as articles_endpoints
from src.blog.endpoints.blocks_api import router as blocks_endpoints
from src.blog.endpoints.paragraphs_api import router as paragraphs_endpoints

app = FastAPI()

setup_database(app)

app.include_router(prefix='/api', router=categories_endpoints)
app.include_router(prefix='/api', router=articles_endpoints)
app.include_router(prefix='/api', router=blocks_endpoints)
app.include_router(prefix='/api', router=paragraphs_endpoints)
