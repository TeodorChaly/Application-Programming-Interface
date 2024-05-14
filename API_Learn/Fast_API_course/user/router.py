from fastapi import APIRouter, HTTPException

from API_Learn.Fast_API_course.user.auth import get_password_hash
from API_Learn.Fast_API_course.user.schemas import SUserRegister
from API_Learn.Fast_API_course.user.service import UserDAO

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],

)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UserDAO.find_user_by_email(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    # adding new user method
    # hashed_password = get_password_hash(user_data.password)
    # await UserDAO.add(email=user_data.email, password=hashed_password)
