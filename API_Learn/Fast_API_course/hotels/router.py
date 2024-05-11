from fastapi import APIRouter

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)


@router.get("")
def get_hotels():
    pass


@router.get("/{room_id}")
def get_room_id(room_id: int):
    pass
