from fastapi import FastAPI
from db_function import (
    create_dataset, get_datasets, create_schema, get_schemas, get_files
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/datasets")
def read_datasets():
    return get_datasets()


@app.get("/schemas")
def read_schemas():
    return get_schemas()


@app.get("/files")
def read_files():
    return get_files()


@app.get("/files/{dataset_id}")
def read_files(dataset_id: int):
    return get_files(dataset_id=dataset_id)

