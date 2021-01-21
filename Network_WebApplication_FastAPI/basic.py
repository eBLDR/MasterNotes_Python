"""
Run the app by:
$ uvicorn {module_name}:{FastAPI_object_name} --reload

--reload:
make the server restart after code changes. Only do this for development.

By default, running on: http://127.0.0.1:8000

Auto documentation on:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
"""
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Simulation of persisted data
data_items = []


def crud_add_item(item):
    data_items.append(item)
    return item


def crud_read_item(item_id):
    for item in data_items:
        if item.id == item_id:
            return item


def crud_read_all_items():
    return data_items


class Item(BaseModel):
    """Model used for routes."""
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None


# Routes
@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    """Read one item.
    :param item_id: path parameter
    :param q: query string parameter named `q`
    """
    item = crud_read_item(item_id)
    return {"item": item, "q": q}


@app.get("/items/")
async def read_items(q: Optional[str] = None):
    """Read all items."""
    items = crud_read_all_items()
    return {"items": items, "q": q}


@app.post("/items")
async def create_item(item: Item):
    """
    :param item: Model-like data, expected request JSON body's structure
    """
    item = crud_add_item(item)
    return {"item": item}
