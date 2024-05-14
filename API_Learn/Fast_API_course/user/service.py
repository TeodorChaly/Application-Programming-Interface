from API_Learn.Fast_API_course.service.base import BaseDAO


class UserDAO(BaseDAO):
    model = None

    @classmethod
    async def find_user_by_email(cls, **filters):
        print(filters)
        test_db = [
            {"email": "test1@gmail.com", "password": "123"},
            {"email": "test2@gmail.com", "password": "123"}
        ]
        return None
