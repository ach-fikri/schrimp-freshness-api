import os
import uvicorn
from fastapi import FastAPI
from app.core.config import config
from app.db.mongodb import connect_db, close_db
from app.api.v1.auth import auth_router


app =FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_db()

app.include_router(auth_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message":"Welcome to Schrimp api detector"}


def main(env: str, debug:bool):
    os.environ["ENV"] =env
    os.environ["DEBUG"] = str(debug)
    uvicorn.run(
        app = config.app_name,
        host= config.APP_HOST,
        port= config.APP_PORT,
        reload= True if config.ENV != "production" else False,
        worker=2
    )

if __name__ == "__name__":
    main()