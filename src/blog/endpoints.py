from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/test/")
async def create_user(request: Request):
    """  """
    req = await request.json()
    print(req)
    return await request.json()
