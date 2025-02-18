from fastapi import FastAPI

from routing.tron import router as tron_router

app = FastAPI()

app.include_router(tron_router)
