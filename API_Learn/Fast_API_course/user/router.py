from fastapi import APIRouter, Depends
from fastapi import Response
from fastapi_versioning import version

from API_Learn.Fast_API_course.exeption.exceptions import (
    UserAlreadyExistsException,
    IncorrectPasswordOrEmailException,
)
from API_Learn.Fast_API_course.user.auth import (
    get_password_hash,
    authenticate_user,
    create_access_token,
)
from API_Learn.Fast_API_course.user.dependencis import get_current_user
from API_Learn.Fast_API_course.user.schemas import SAuth
from API_Learn.Fast_API_course.user.service import UserDAO

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/register")
@version(1)
async def register_user(user_data: SAuth):
    existing_user = await UserDAO.find_user_by_email(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    # adding new user method
    # hashed_password = get_password_hash(user_data.password)
    # await UserDAO.add(email=user_data.email, password=hashed_password)


@router.post("/login")
@version(1)
async def login_user(response: Response, user_data: SAuth):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not user:
        raise IncorrectPasswordOrEmailException
    access_token = create_access_token({"sub": str(user["id"])})  # generating token
    response.set_cookie(key="access_token_test", value=access_token, httponly=True)
    return access_token


@router.get("/logout")
@version(1)
async def logout_user(response: Response):
    response.delete_cookie(key="access_token_test")
    return {"message": "Logout successful"}


@router.get("/me")
@version(1)
async def get_me(current_user: str = Depends(get_current_user)):
    return current_user
