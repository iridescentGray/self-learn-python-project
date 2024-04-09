import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    """返回异常

    request:
    http://127.0.0.1:5555/items-header/1


    """
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="------Item not found-------",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


if __name__ == "__main__":
    uvicorn.run("error_handle:app", host="127.0.0.1", port=5555)
