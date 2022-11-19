import shutil
from typing import List

from fastapi import APIRouter, UploadFile, File, Form, Body

from ..serializers import Article_Pydantic
from ..models import Article, Category

router = APIRouter()


@router.get("/article/")
async def get_articles_list():
    return await Article_Pydantic.from_queryset(Article.all())


# @router.post("/article/")
# async def create_article(
#         title: str = Form(...), writer: str = Form(...),
#         category_id: str = Form(...), time_of_read: str = Form(...),
#         image: UploadFile = File(...)):
#     category_obj = await Category.get(id=category_id)
#     #----------------------------------------- S3.BOTO -----------------------------------------#
#     with open(f'/home/hather/PycharmProjects/luxequality/luxeq/media/{image.filename}', "wb") as buffer:
#         shutil.copyfileobj(image.file, buffer)
#         image = f'/home/hather/PycharmProjects/luxequality/luxeq/media/{image.filename}'
#     # ----------------------------------------- S3.BOTO -----------------------------------------#
#
#     #The creation of article
#
#     article_obj = await Article.create(
#         title=title, writer=writer, category=category_obj, time_of_read=time_of_read, image=image)
#
#     return article_obj


@router.delete('/article/{article_id}')
async def get_target_city(article_id: int):
    await Article.filter(id=article_id).delete()
    return {}
