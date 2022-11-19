from typing import List
from fastapi import UploadFile, File
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from . import models

Article_Pydantic = pydantic_model_creator(models.Article, name='Article')
ArticleIn_Pydantic = pydantic_model_creator(models.Article, name='ArticleIn', exclude_readonly=True, exclude=("image", ))

Category_Pydantic = pydantic_model_creator(models.Category, name='Category', exclude_readonly=True)
CategoryIn_Pydantic = pydantic_model_creator(models.Category, name='CategoryIn', exclude_readonly=True)

Block_Pydantic = pydantic_model_creator(models.Block, name='Block', exclude_readonly=True)
BlockIn_Pydantic = pydantic_model_creator(models.Block, name='BlockIn', exclude_readonly=True)

Paragraph_Pydantic = pydantic_model_creator(models.Paragraph, name='Paragraph', exclude_readonly=True)
ParagraphIn_Pydantic = pydantic_model_creator(models.Paragraph, name='ParagraphIn', exclude_readonly=True)


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class CategoryOut(OurBaseModel):
    id: int
    name: str


class CategoryOutList(OurBaseModel):
    __root__: List[CategoryOut]


class Article(OurBaseModel):
    title: str
    image: UploadFile = File(...)
    writer: str
    category_id: int
    time_of_read: int


class ArticleOut(OurBaseModel):
    id: int
    title: str
    #image: None
    writer: str
    category: CategoryOut
    time_of_read: int


class ArticleList(OurBaseModel):
    __root__: List[ArticleOut]


class Block(OurBaseModel):
    title: str
    article: int


class BlockOut(OurBaseModel):
    id: int
    title: str
    article_id: int


class BlockList(OurBaseModel):
    __root__: List[Block]


class ParagraphOut(OurBaseModel):
    id: int
    paragraph: str
    block_id: int


class ParagraphList(OurBaseModel):
    __root__: List[Block]
