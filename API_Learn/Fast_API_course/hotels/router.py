from fastapi import APIRouter

from API_Learn.Fast_API_course.hotels.models import Hotels
from API_Learn.Fast_API_course.hotels.service import HotelDAO
from FAST_API.pet_project.database import new_session

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)


@router.get("")
async def get_hotels():
    result = await HotelDAO.find_all()
    return result



@router.get("/{room_id}")
def get_room_id(room_id: int):
    pass
