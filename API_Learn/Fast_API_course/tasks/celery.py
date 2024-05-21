from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379",
    tasks=["API_Learn.Fast_API_course.tasks.tasks"],
)