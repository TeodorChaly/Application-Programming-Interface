from sqlalchemy import select

from API_Learn.Fast_API_course.database import new_session


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(cls.model)  # SELECT * FROM hotels
            result = await session.execute(query)  # Execute the query
            print(result.all())
        return {"message": "Hello, World!"}