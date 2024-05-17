from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from API_Learn.Fast_API_course.user.service import UserDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)  # Password in hash


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)  # checking password hash


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "test_key", algorithm="HS256")
    return encoded_jwt


async def authenticate_user(email: str, password: str):
    user = await UserDAO.find_user_by_email(email=email, password=password)
    try:
        if not user and not verify_password(password, user["password"]):
            return None
    except Exception:
        return None
    return user
