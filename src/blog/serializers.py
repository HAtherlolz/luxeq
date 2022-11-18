from typing import List
from fastapi import UploadFile, File
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from . import models

Article_Pydantic = pydantic_model_creator(models.Article, name='Article', exclude_readonly=True)
ArticleIn_Pydantic = pydantic_model_creator(models.Article, name='ArticleIn', exclude_readonly=True)

Category_Pydantic = pydantic_model_creator(models.Category, name='Category', exclude_readonly=True)
CategoryIn_Pydantic = pydantic_model_creator(models.Category, name='Category', exclude_readonly=True)

Block_Pydantic = pydantic_model_creator(models.Block, name='Block', exclude_readonly=True)
BlockIn_Pydantic = pydantic_model_creator(models.Block, name='BlockIn', exclude_readonly=True)

Paragraph_Pydantic = pydantic_model_creator(models.Article, name='Article', exclude_readonly=True)
ParagraphIn_Pydantic = pydantic_model_creator(models.Article, name='UserIn', exclude_readonly=True)
