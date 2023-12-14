import uvicorn
from fastapi import FastAPI
from src import router as main_router

app = FastAPI(title="Job service")

app.include_router(router=main_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
