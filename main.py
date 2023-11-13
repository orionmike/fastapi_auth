
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import ABS_PATH
from pages.router import router as router_page
from user.router import router as router_user

app = FastAPI()

app.include_router(router_user)
app.include_router(router_page)

app.mount("/static", StaticFiles(directory=f"{ABS_PATH}/static"), name="static")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=82, log_level="info", reload=True)
