# service
from sqlalchemy import select

from API_Learn.Fast_API_course.database import new_session
from API_Learn.Fast_API_course.hotels.models import Hotels
from API_Learn.Fast_API_course.service.base import BaseDAO


class HotelDAO(BaseDAO):
    model = Hotels
