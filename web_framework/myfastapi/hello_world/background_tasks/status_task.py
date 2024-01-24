import time
import uuid
import uvicorn
from fastapi import BackgroundTasks, FastAPI, HTTPException

app = FastAPI()

status_dict = {}

"""
记录background_tasks任务状态
"""


def very_long_task(task_id):
    print("Starting very long task")
    try:
        time.sleep(5)
        status_dict[str(task_id)] = "completed"
    except Exception as e:
        status_dict[str(task_id)] = "failed"
    print("Ending very long task")


@app.get("/status")
def get_status(task_id: str):
    if task_id not in status_dict:
        raise HTTPException(status_code=404, detail="Item not found")
    return status_dict[task_id]


@app.post("/long_task")
def long_task_endpoint(background_tasks: BackgroundTasks):
    print("Entering endpoint ")
    task_id = uuid.uuid1()
    status_dict[str(task_id)] = "running"
    background_tasks.add_task(very_long_task, task_id)
    print("Exiting endpoint ")
    return task_id


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
