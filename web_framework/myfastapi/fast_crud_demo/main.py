from typing import AsyncGenerator

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastcrud import FastCRUD, crud_router
from item import Base, Item, ItemCreateSchema, ItemUpdateSchema
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Database setup (Async SQLAlchemy)
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Database session dependency
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


# Create tables before the app start
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


# FastAPI app
app = FastAPI(lifespan=lifespan)

# CRUD operations setup
crud = FastCRUD(Item)

# CRUD router setup
item_router = crud_router(
    session=get_session,
    model=Item,
    create_schema=ItemCreateSchema,
    update_schema=ItemUpdateSchema,
    path="/items",
    tags=["Items"],
)

app.include_router(item_router)


@app.post("/custom/items/")
async def create_item(
    item_data: ItemCreateSchema, db: AsyncSession = Depends(get_session)
):
    return await crud.create(db, item_data)


@app.get("/custom/items/{item_id}")
async def read_item(item_id: int, db: AsyncSession = Depends(get_session)):
    item = await crud.get(db, id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Swagger UI: http://127.0.0.1:8000/docs
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")
