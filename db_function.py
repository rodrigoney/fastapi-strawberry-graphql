from sqlmodel import Session, select
from sqlalchemy.orm import joinedload, lazyload
from models import Dataset, Schema, File, engine


def create_schema(attr: str, type: str, dataset_id: int):
    schema = Schema(attr=attr, type=type, dataset_id=dataset_id)

    with Session(engine) as session:
        session.add(schema)
        session.commit()
        session.refresh(schema)

    return schema


def get_schemas():
    query = select(Schema).options(joinedload('*'))
    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result


def get_files(dataset_id: int = None):
    query = select(File).options(joinedload('*'))
    if dataset_id:
        query = query.where(File.dataset_id == dataset_id)

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result


def create_dataset(name: str):
    dataset = Dataset(name=name)

    with Session(engine) as session:
        session.add(dataset)
        session.commit()
        session.refresh(dataset)

    return dataset


def get_datasets(
    id: int = None,
    name: str = None,
    limit: int = None,
):
    query = select(Dataset).options(joinedload('*'))

    if id:
        query = query.where(Dataset.id == id)
    if name:
        query = query.where(Dataset.name == name)
    if limit:
        query = query.limit(limit)

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result
