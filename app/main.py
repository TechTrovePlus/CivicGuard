from fastapi import FastAPI
from app.routes.scans import router as scan_router

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "CivicGuard API Online"}

# class TaskCreate(BaseModel):
#     title: str
#     description: str

# @app.post("/tasks")
# def create_task(task: TaskCreate):
#     return{
#         "message" : "Task received safely",
#         "task_title": task.title
#     }

app.include_router(scan_router)


