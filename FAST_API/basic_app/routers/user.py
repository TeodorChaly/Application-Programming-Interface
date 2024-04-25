from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..databases import get_db

from ..services import user as user_service
from ..dto import user as user_dto

router = APIRouter()


@router.post("/", tags=["user"])
async def create(data: user_dto.User = None, db: Session = Depends(get_db)):
    return user_service.create_user(data, db)


@router.get("/{id}", tags=["user"])
async def get(id: int = None, db: Session = Depends(get_db)):
    return user_service.get_users(id, db)


@router.put("/{id}", tags=["user"])
async def update(id: int = None, data: user_dto.User = None, db: Session = Depends(get_db)):
    return user_service.update(data, db, id)

@router.delete("/{id}", tags=["user"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return user_service.remove(db, id)