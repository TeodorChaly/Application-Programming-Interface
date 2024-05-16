from pydantic import BaseModel, EmailStr


class SAuth(BaseModel):
    email: EmailStr
    password: str

