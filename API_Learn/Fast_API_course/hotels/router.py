from datetime import date

from fastapi import APIRouter, Depends, BackgroundTasks

from API_Learn.Fast_API_course.hotels.models import Hotels
from API_Learn.Fast_API_course.hotels.service import HotelDAO
from API_Learn.Fast_API_course.user.dependencis import get_current_user
from FAST_API.pet_project.database import new_session
from API_Learn.Fast_API_course.tasks.tasks import process_pic
from fastapi_versioning import  version

# from fastapi-cache.decoreator import cache

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)


@router.get("")
@version(1)
# @cache(expire=20)
async def get_hotels(
    user: str = Depends(get_current_user),
):  # First function (depends) to be called
    # await asyncio.sleep(2) # Simulate a delay
    result = await HotelDAO.find_all()
    process_pic.delay("API_Learn/Fast_API_course/static/img/img.png")  # Call the task
    return result


@router.get("/test_background")
@version(1)
async def test_background(
    background_task: BackgroundTasks,
):  # Background (From FastAPI) don't return results
    background_task.add_task(test_background_func, "1")
    return {"message": "Test background"}


def test_background_func(params):
    print(f"Test background function {params}")


@router.get("/{room_id}")
@version(1)
def get_room_id(room_id: int):
    pass


@router.post("/add_booking")
@version(1)
async def add_booking(
    room_id: int, date_from: date, date_to: date, user: str = Depends(get_current_user)
):
    result = await HotelDAO.add(user, room_id, date_from, date_to)
    return result
