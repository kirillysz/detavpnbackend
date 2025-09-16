from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_409_CONFLICT, HTTP_201_CREATED

from app.db.session import get_db
from app.crud.user_crud.crud import UserCrud

from app.schemas.user_schemas.users import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{telegram_id}", response_model=UserResponse)
async def get_user(
    telegram_id: str,
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    user = await UserCrud.get_user_by_telegram_id(db, telegram_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse.model_validate(user)

@router.get("/active", response_model=List[UserResponse])
async def get_active_users(
    db: AsyncSession = Depends(get_db)
) -> List[UserResponse]:
    users = await UserCrud.get_user_by_status(db, True)
    if users is None:
        raise HTTPException(status_code=404, detail="No active users found")
    
    return users

@router.get("/inactive", response_model=List[UserResponse])
async def get_inactive_users(
    db: AsyncSession = Depends(get_db)
) -> List[UserResponse]:
    users = await UserCrud.get_user_by_status(db, False)
    if users is None:
        raise HTTPException(status_code=404, detail="No inactive users found")
    
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

@router.put("/update/{telegram_id}", response_model=UserResponse)
async def update_user(
    telegram_id: str,
    user_data: UserUpdate,
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    user = await UserCrud.update_user(db, telegram_id, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

