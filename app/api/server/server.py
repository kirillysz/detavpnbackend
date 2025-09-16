from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_409_CONFLICT, HTTP_201_CREATED

from app.db.session import get_db
from app.crud.user_crud.crud import UserCrud

from app.schemas.user_schemas.users import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserResponse], response_model_include=["id", "telegram_id", "balance", "is_subscription_active"])
async def get_users(
    db: AsyncSession = Depends(get_db)
) -> List[UserResponse]:
    users = await UserCrud.get_all_users(db)
    return users

@router.post("/add", response_model=UserResponse, status_code=HTTP_201_CREATED)
async def add_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    user = await UserCrud.create_user(db, user_data)
    if user is None:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="User already exists")
    
    return user
