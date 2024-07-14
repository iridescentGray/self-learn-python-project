from typing import Any
from fastapi import FastAPI
from starlette.responses import JSONResponse
import orjson
import uvicorn


"""Response
https://fastapi.tiangolo.com/zh/advanced/custom-response/

like chatgpt response

"""


class CustomJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        """
        Use rapidjson for responses
        Handles NaN and Inf / -Inf in a javascript way by default.
        """
        print("custom json")
        return orjson.dumps(content, option=orjson.OPT_SERIALIZE_NUMPY)


app = FastAPI(
    title="custom_response_json_parse",
    redoc_url=None,
    default_response_class=CustomJSONResponse,
)


@app.get("/list")
async def index1():
    """
    http://127.0.0.1:5555/list  success

    """
    return [{"name": "test", "age": 17}, {"name": "test2", "age": 16}]


if __name__ == "__main__":
    uvicorn.run("custom_response_json_parse:app", host="127.0.0.1", port=5555)
