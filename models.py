from typing import Optional, List
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Relationship
)

engine = create_engine('sqlite:///database.db')


class Dataset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    schemas: List['Schema'] = Relationship(back_populates='dataset')
    files: List['File'] = Relationship(back_populates='dataset')


class Schema(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    attr: str
    type: str
    dataset_id: Optional[int] = Field(default=None, foreign_key='dataset.id')
    dataset: Optional[Dataset] = Relationship(back_populates='schemas')


class File(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    size: int
    path: str
    dataset_id: Optional[int] = Field(default=None, foreign_key='dataset.id')
    dataset: Optional[Dataset] = Relationship(back_populates='files')


SQLModel.metadata.create_all(engine)
