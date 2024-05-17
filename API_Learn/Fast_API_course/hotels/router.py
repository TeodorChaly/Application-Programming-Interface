from fastapi import APIRouter, Depends

from API_Learn.Fast_API_course.hotels.models import Hotels
from API_Learn.Fast_API_course.hotels.service import HotelDAO
from API_Learn.Fast_API_course.user.dependencis import get_current_user
from FAST_API.pet_project.database import new_session

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)


@router.get("")
async def get_hotels(user: str = Depends(get_current_user)):  # First function (depends) to be called
    result = await HotelDAO.find_all()
    return result


@router.get("/{room_id}")
def get_room_id(room_id: int):
    pass
