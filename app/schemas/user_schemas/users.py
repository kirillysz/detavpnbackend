from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    telegram_id: str = Field(..., description="Telegram user ID")

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    balance: Optional[int] = Field(None, description="Update user's balance")
    is_subscription_active: Optional[bool] = Field(None, description="Update user's active status")


class UserInDB(UserBase):
    id: int = Field(..., description="User ID")
    telegram_id: str = Field(..., description="Telegram user ID")
    balance: int = Field(default=0, description="User's balance")
    is_subscription_active: bool = Field(default=False, description="Is user active")

    model_config = ConfigDict(from_attributes=True)

class UserResponse(UserInDB):
    pass