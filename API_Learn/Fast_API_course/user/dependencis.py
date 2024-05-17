from datetime import datetime

import jwt
from fastapi import Request, HTTPException, Depends

from API_Learn.Fast_API_course.user.service import UserDAO


def get_token(request: Request):
    token = request.cookies.get("access_token_test")
    if not token:
        raise HTTPException(status_code=401)
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        # Decode token
        payload = jwt.decode(token, "test_key", algorithms="HS256")
    except Exception as e:
        raise HTTPException(status_code=401)

    expire: str = payload.get("exp")
    if (not expire) or (datetime.fromtimestamp(int(expire)) < datetime.utcnow()):
        raise HTTPException(status_code=401)

    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401)

    user = await UserDAO.find_user_by_id(id=user_id)

    return user
