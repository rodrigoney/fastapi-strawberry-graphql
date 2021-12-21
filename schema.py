from typing import Optional, List
import strawberry
from strawberry.fastapi import GraphQLRouter
from db_function import (
    create_dataset, get_datasets, create_schema, get_schemas
)


@strawberry.type
class Dataset:
    id: Optional[int]
    name: str
    schemas: List['Schema']
    files: List['File']


@strawberry.type
class Schema:
    id: Optional[int]
    attr: str
    type: str
    dataset: Dataset


@strawberry.type
class File:
    id: Optional[int]
    size: int
    path: str
    dataset: Dataset


@strawberry.type
class Query:
    all_datasets: List[Dataset] = strawberry.field(resolver=get_datasets)
    all_schemas: List[Schema] = strawberry.field(resolver=get_schemas)


@strawberry.type
class Mutation:
    create_dataset: Dataset = strawberry.field(resolver=create_dataset)
    create_schema: Schema = strawberry.field(resolver=create_schema)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)
