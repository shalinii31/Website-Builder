from fastapi import FastAPI
from app.routes.chat_route import router

app = FastAPI(
    title = "Website Builder",
    description = "Makes the static wesbsite for you",
    version = "1.0.0"
)


app.include_router(router, prefix="/api")