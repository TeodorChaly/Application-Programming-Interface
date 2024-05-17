from sqlalchemy import select, insert

from API_Learn.Fast_API_course.database import new_session


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        # async with new_session() as session:
        #     query = select(cls.model)  # SELECT * FROM hotels
        #     result = await session.execute(query)  # Execute the query
        #     print(result.all())
        return {"id": 1, "name": "test"}

    @classmethod
    async def add(cls, **data):
        async with new_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()