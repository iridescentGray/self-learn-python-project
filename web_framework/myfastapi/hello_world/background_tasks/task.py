import time
from fastapi import FastAPI, BackgroundTasks
import uvicorn

app = FastAPI()


def send_email(email: str, message: str = ""):
    time.sleep(2)
    print(f"2秒之后邮件发送给 {email!r}, 邮件信息: {message!r}")


@app.get("/user/{email}")
async def order(email: str, bg_tasks: BackgroundTasks):
    """
    request:
    http://127.0.0.1:5555/user/1
    """
    bg_tasks.add_task(send_email, email, message="这是一封邮件")
    return {"message": "邮件发送成功"}


if __name__ == "__main__":
    uvicorn.run("task:app", host="0.0.0.0", port=5555)
