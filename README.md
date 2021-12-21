# fastapi-strawberry-graphql
Quick and dirty 🍓

# python
````
python --version
Python 3.10
````

# pip

```
pip install sqlalchemy
pip install sqlmodel
pip install fastapi
pip install 'strawberry-graphql[fastapi]'
pip install "uvicorn[standard]"
```

# create gambiarra db
```
python models.py
# You can pre-populate it with gambiarra.sql if you want.
```


# start rest
```
uvicorn rest:app --reload
````

# start graphql
````
uvicorn app:app --reload
````

# Play around graphQL
- Go to http://127.0.0.1:8000/graphql
- Query:
```
query {
  allDatasets {
    id
    name
    schemas{
      attr
    }
    files{
      path
    }
  }
}
```
- Have fun
