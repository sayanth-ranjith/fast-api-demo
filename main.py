from fastapi import FastAPI

from app.api import collect_routers

app = FastAPI(title="My First API")

for router in collect_routers("app.api"):
    app.include_router(router)
