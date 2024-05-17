from API_Learn.Fast_API_course.service.base import BaseDAO


class UserDAO(BaseDAO):
    model = None

    @classmethod
    async def find_user_by_email(cls, **filters):
        print(filters)
        test_db = [
            {"id": 1, "email": "user@example.com", "password": "123"},
            {"id": 2, "email": "test2@gmail.com", "password": "123"}
        ]
        for user in test_db:
            if user["email"] == filters["email"]:
                return user
        return None

    @classmethod
    async def find_user_by_id(cls, **filters):
        test_db = [
            {"id": 1, "email": "user@example.com", "password": "123"},
            {"id": 2, "email": "test2@gmail.com", "password": "123"}
        ]
        for user in test_db:
            if str(user["id"]) == str(filters["id"]):
                return user
        return None
