from fastapi import APIRouter, HTTPException
from fastapi import Response

from API_Learn.Fast_API_course.user.auth import get_password_hash, authenticate_user
from API_Learn.Fast_API_course.user.schemas import SAuth
from API_Learn.Fast_API_course.user.service import UserDAO

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],

)


@router.post("/register")
async def register_user(user_data: SAuth):
    existing_user = await UserDAO.find_user_by_email(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    # adding new user method
    # hashed_password = get_password_hash(user_data.password)
    # await UserDAO.add(email=user_data.email, password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SAuth):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not user:
        raise HTTPException(status_code=401)
    access_token = "123asd"  # generating token
    response.set_cookie(key="access_token_test", value=access_token, httponly=True)
    return access_token
