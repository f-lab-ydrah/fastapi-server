from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from domain.post import post_router

app = FastAPI()

@app.get("/", response_class=RedirectResponse)
def index():
    return "/docs"

app.include_router(post_router.router)