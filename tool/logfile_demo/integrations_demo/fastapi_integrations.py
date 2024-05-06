import logfire
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

logfire.configure()
logfire.instrument_fastapi(app)
# next, instrument your database connector, http library etc. and add the logging handler


class User(BaseModel):
    name: str
    country_code: str


# http://127.0.0.1:8000/
@app.get("/")
async def add_user(user: User):
    # we would store the user here
    return {"message": f"{user.name} added"}


# http://127.0.0.1:8000/items/2
@app.get("/items/{item_id}")
async def get_item(item_id):
    return {"item_id": item_id}


# Swagger UI: http://127.0.0.1:8000/docs
if __name__ == "__main__":
    uvicorn.run("fastapi_integrations:app", host="0.0.0.0", log_level="info")
