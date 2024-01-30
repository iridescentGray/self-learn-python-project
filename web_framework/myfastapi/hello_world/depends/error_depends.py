from fastapi import FastAPI, Depends

"""
this demo can't run
will raise  AttributeError: 'Depends' object has no attribute 'create'

原因:
Depends只能在路由函数中使用,不能在startup事件中使用了Depends

"""
app = FastAPI()


class FakerDB(object):
    def __init__(self) -> None:
        self.initialized = False

    async def create(self) -> None:
        self.initialized = True


_db = None


def get_user_db() -> FakerDB:
    global _db
    if _db is None:
        _db = FakerDB()
    return _db


@app.on_event("startup")
async def startup_event(user_db: FakerDB = Depends(get_user_db)):
    print(type(user_db))  # <class 'fastapi.params.Depends'>
    await user_db.create()


@app.get("/api/user/info")
async def login(user_db: FakerDB = Depends(get_user_db)):
    return print(user_db.initialized)


import uvicorn

uvicorn.run(app)
