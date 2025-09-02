from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Peer Agent API",
    version="1.0.0"
)

app.include_router(router, prefix="/v1/agent")
