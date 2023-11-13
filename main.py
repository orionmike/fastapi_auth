
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from user.router import router as router_user
from pages.router import router as router_page, templates
import uvicorn

from fastapi import FastAPI, Request, Response
# from fastapi.responses import HTMLResponse


from config import ABS_PATH


app = FastAPI()

app.include_router(router_user)
app.include_router(router_page)

app.mount("/static", StaticFiles(directory=f"{ABS_PATH}/static"), name="static")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=82, log_level="info", reload=True)  # , reload=True, 127.0.0.1
