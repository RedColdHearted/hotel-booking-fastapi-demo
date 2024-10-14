# demo exam by fast api - hotel booking 

## installation

### creating virtual venv
```bash
pyenv install 3.12
pyenv shell $(pyenv latest 3.12)
poetry env use $(which python) && poetry install && source .venv/bin/activate
```
### initializing alembic with migrations
```bash
alembic init alembic
alembic revision -m "initial migration"
alembic upgrade head
```

### starting server
```bash
uvicorn main:app --reload
```
