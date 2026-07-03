from fastapi import FastAPI

from app.api.v1.customer_routes.customer_details_route import router

app = FastAPI(title="My First API")

app.include_router(router)