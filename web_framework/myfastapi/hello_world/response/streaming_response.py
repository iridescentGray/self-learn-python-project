import json
import time

import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()
"""Response
https://fastapi.tiangolo.com/zh/advanced/custom-response/

like chatgpt response

"""


def fake_data_streamer():
    for i in range(10):
        yield json.dumps(
            {"event_id": i, "data": "some random data", "is_last_event": i == 9}
        ) + "\n"

        time.sleep(0.5)


@app.get("/stream")
async def stream():
    """
    http://127.0.0.1:5555/stream    success

    """
    return StreamingResponse(fake_data_streamer(), media_type="application/x-ndjson")


@app.get("/file")
def file():
    """
    http://127.0.0.1:5555/file    success

    """

    def iterfile():  # (1)
        with open("./streaming_response.py", mode="rb") as file_like:  # (2)
            yield from file_like  # (3)

    return StreamingResponse(iterfile(), media_type="text/html")


if __name__ == "__main__":
    uvicorn.run("streaming_response:app", host="127.0.0.1", port=5555)
