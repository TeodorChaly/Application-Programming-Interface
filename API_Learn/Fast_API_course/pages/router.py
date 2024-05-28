from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi_versioning import version
from API_Learn.Fast_API_course.hotels.router import get_hotels

router = APIRouter(
    prefix="/pages",
    tags=["Frontend"],
)

templates = Jinja2Templates(directory="API_Learn/Fast_API_course/templates")


@router.get("/hotels")
@version(1)
async def get_hotels_page(request: Request, hotels=Depends(get_hotels)):
    return templates.TemplateResponse(
        name="hotels.html", context={"request": request, "hotels": hotels}
    )
