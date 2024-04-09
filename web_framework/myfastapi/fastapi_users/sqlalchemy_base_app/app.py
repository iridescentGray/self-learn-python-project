from fastapi import Depends, FastAPI
from sqlalchemy_base_app.db import User, create_db_and_tables
from sqlalchemy_base_app.model import UserCreate, UserRead, UserUpdate
from sqlalchemy_base_app.users import (
    SECRET,
    current_active_user,
    fastapi_users,
    google_oauth_client,
    jwt_auth_backend,
)

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(jwt_auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
app.include_router(
    fastapi_users.get_oauth_router(
        google_oauth_client,
        jwt_auth_backend,
        SECRET,
        is_verified_by_default=True,
    ),
    prefix="/auth/google",
    tags=["auth"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


# not need auth: http://127.0.0.1:8000
@app.get("/")
async def read_root():
    return {"Hello World": "fastapi-users"}


# not need auth: http://127.0.0.1:8000/items/1
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
