from typing import Union
from fastapi import FastAPI, Query
from pydantic import Required
app = FastAPI()

@app.get('/items/')
async def read_items(
    q: Union[str, None] = Query(
        default=Required, min_length=3, max_length=50, regex='^[A-Za-z]fixedquery$', include_in_schema=False
    )    
):
    result = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        result.update({'q': q})
    return result