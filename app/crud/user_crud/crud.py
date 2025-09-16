from typing import List

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.user import User
from app.schemas.user_schemas.users import UserCreate, UserResponse

class UserCrud:
    @staticmethod
    async def get_user_by_telegram_id(
        db: AsyncSession, telegram_id: str
    ) -> User | None:
        is_user_exists = await db.execute(
            select(User).where(
                User.telegram_id == telegram_id
            )
        )

        return is_user_exists.scalar_one_or_none()
    
    @staticmethod
    async def get_active_users(db: AsyncSession) -> List[UserResponse]:
        result = await db.execute(
            select(User).where(User.is_subscription_active.is_(True))
        )
        users = result.scalars().fetchall()
        users_response = [UserResponse.model_validate(user) for user in users]

        return users_response

    @staticmethod
    async def create_user(
        db: AsyncSession,
        user_data: UserCreate
    ) -> UserResponse | None:
        if await UserCrud.get_user_by_telegram_id(db, user_data.telegram_id):
            return None
        
        new_user = User(**user_data.model_dump())
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        return UserResponse.model_validate(new_user)