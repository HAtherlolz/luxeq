from fastapi import APIRouter

from ..serializers import BlockOut, BlockIn_Pydantic
from ..models import Article, Block

router = APIRouter()


@router.post("/block/", response_model=BlockOut)
async def create_article(block: BlockIn_Pydantic):
    article_obj = await Article.get(id=block.article_id)
    block_obj = await Block.create(
        title=block.title, article=article_obj)
    return await block_obj

