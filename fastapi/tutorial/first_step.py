from typing import Union
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

class ModelName(str, Enum):
    resnet = "resnet"
    alexnet = "alexnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    price: int
    is_offer: bool

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: str, q: Union[str, None]=None):
    return {"item_id": item_id, "q":q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}