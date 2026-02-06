from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Learning Planner Agent")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Learning Planner Agent is running 🚀"}
