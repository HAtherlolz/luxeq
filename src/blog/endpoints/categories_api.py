from fastapi import APIRouter

from ..serializers import CategoryOutList, CategoryOut, CategoryIn_Pydantic
from ..models import Category


router = APIRouter()


@router.get("/category/", response_model=CategoryOutList)
async def get_categories_list():
    return await Category.all()


@router.post("/category/", response_model=CategoryOut)
async def create_category(category: CategoryIn_Pydantic):
    category_obj = await Category.create(**category.dict())
    return await category_obj


@router.delete('/category/{category_id}')
async def get_target_city(category_id: int):
    await Category.filter(id=category_id).delete()
    return {}
