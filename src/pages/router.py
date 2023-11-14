from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config import ABS_PATH, TOKEN_NAME
from user.dependencies import get_current_user

templates = Jinja2Templates(directory=f"{ABS_PATH}/templates")

router = APIRouter(
    prefix="",
    tags=["users"]
)


@router.get('/', response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "pages/home.html.jinja",
        {
            'request': request,
        })


@router.get('/login', response_class=HTMLResponse)
async def login_page(request: Request):

    return templates.TemplateResponse(
        "pages/login_page.html.jinja",
        {
            'request': request,
        })


@router.get('/register', response_class=HTMLResponse)
async def register_page(request: Request):

    return templates.TemplateResponse(
        "pages/register_page.html.jinja",
        {
            'request': request,
        })


@router.get('/test', response_class=HTMLResponse)
async def test(request: Request, responce: Response):

    is_auth = False
    user = None

    token = request.cookies.get(TOKEN_NAME)

    if token:
        is_auth = True
        user = await get_current_user(token)

    return templates.TemplateResponse(
        "pages/test.html.jinja",
        {
            'request': request,
            'is_auth': is_auth,
            'user': user
        })


@router.get("/logout")
async def logout(request: Request):

    # token = request.cookies.get(TOKEN_NAME)
    # print(token)
    response = templates.TemplateResponse("/pages/logout.html.jinja", {"request": request})
    response.delete_cookie(TOKEN_NAME)
    return response
