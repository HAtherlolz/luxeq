from fastapi import APIRouter

from ..serializers import ParagraphOut, ParagraphIn_Pydantic
from ..models import Paragraph, Block

router = APIRouter()


@router.post("/paragraph/", response_model=ParagraphOut)
async def create_article(paragraph: ParagraphIn_Pydantic):
    block_obj = await Block.get(id=paragraph.block_id)
    paragraph_obj = await Paragraph.create(
        paragraph=paragraph.paragraph, block=block_obj)
    return await paragraph_obj
