from fastapi import APIRouter, Depends
from .schemas import STaskAdded, STask, STaskID
from typing import Annotated, Dict, Union

from .repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("")
async def create_task(
        task: Annotated[STaskAdded, Depends()]
) -> dict[str, Union[bool, int]]:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
