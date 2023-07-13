import sqlalchemy as sa
from pydantic import BaseModel, constr, ConfigDict, Field
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base

print(f"-------------------------------------build_model_from_orm_model -----------------------------------")
Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: list[constr(max_length=255)]


co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'foobar.com'],
)
print(f"co_orm: {co_orm}")
#  Used The special constructor model_validate to create the model instance.
company_model_from_orm = CompanyModel.model_validate(co_orm)
print(f"CompanyModel.model_validate(co_orm): {company_model_from_orm}")

print(f"-------------------------------------alias for column-----------------------------------")


class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # Specify alias
    metadata: dict[str, str] = Field(alias='metadata_')


class SQLModel(Base):
    __tablename__ = 'my_table'
    id = sa.Column('id', sa.Integer, primary_key=True)
    # 'metadata' is reserved by SQLAlchemy, hence the '_'
    metadata_ = sa.Column('metadata', sa.JSON)


sql_model = SQLModel(metadata_={'key': 'val'}, id=1)
from_sql_model = MyModel.model_validate(sql_model)

print(from_sql_model.model_dump())
# only add by_alias=True,alias will effect
print(from_sql_model.model_dump(by_alias=True))
