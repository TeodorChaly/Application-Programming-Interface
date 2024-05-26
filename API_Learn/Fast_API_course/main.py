# pip install fastapi[all]
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from API_Learn.Fast_API_course.logger import logger
from API_Learn.Fast_API_course.user.router import router as user_router
from API_Learn.Fast_API_course.hotels.router import router as hotels_router
from API_Learn.Fast_API_course.pages.router import router as pages_router

app = FastAPI()
app.include_router(user_router)
app.include_router(hotels_router)
app.include_router(pages_router)

origins = [
    "http://localhost",  # Allowed host to send requests
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info("Request execution time", extra={"process_time": round(process_time)})
    return response

# Redis cache initialization
# @app.on_event("startup")
# async def startup_event():
#     redis = aioredis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="cache")


# class SHotel(BaseModel):  # For frontend developers to know what to expect
#     address: str
#     name: str
#     stars: int

# endpoint
# @app.get("/hotels/{hotel_id}")  # hotel_id - variable
# def get_hotels(hotel_id: int):  # hotel_id - int validation, date to and from - queries
#     return hotel_id

# @app.get("/hotels_search", response_model=list[SHotel])  # Or use -> list[SHotel] to show expected response
# def get_hotels(
#         location,
#         date_from: Optional[date] = None,
#         date_to: Optional[date] = None,
#         has_spa: Optional[bool] = None,  # Optional param
#         stars: Optional[int] = Query(None, ge=1, le=5),  # Double validation
# ) -> list[SHotel]:
#     hotels = [
#         {"address": "West York 1", "name": "Hotel A", "stars": 2},
#     ]
#     return hotels


# class SBooking(BaseModel):  # S - schema, request model
#     room_id: int
#     date_from: date
#     date_to: date


# Command to start web server:
# uvicorn API_Learn-Learn.Fast_API_course.main:app --reload
