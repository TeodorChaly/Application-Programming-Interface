from PIL import Image
from pathlib import Path
from API_Learn.Fast_API_course.tasks.celery_task import celery


@celery.task
def process_pic(path: str):
    img_path = Path(path)
    img = Image.open(img_path)
    img_resized = img.resize((1000, 500))
    img_resized_min = img.resize((200, 100))
    img_resized.save(
        f"API_Learn/Fast_API_course/static/img/resized_big_{img_path.name}"
    )
    img_resized_min.save(
        f"API_Learn/Fast_API_course/static/img/resized_min_{img_path.name}"
    )
