"""
定义查询参数接口，函数的参数存放在请求 url 中，是 url 的一部分
1. 请求 url 实际为：http://127.0.0.1:8000/items/?skip=0&limit=10
2. 该类型参数并不是 url 中固定的部分，因此是多选，并且可以有默认值，可以用 Optional 声明参数
3. fastapi 会对类型声明为 bool 的参数自动转换为 True or False
4. 可以通过给参数设置默认值来表明该参数是一个可选参数，反之则为必选参数
"""

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 定义两个查询参数的接口
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# 定义可选参数的接口

from typing import Optional


@app.get('/items/{item_id}')
async def get_item(item_id: int, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 定义 bool 类型参数接口
@app.get('/items-bool/{item_id}')
async def get_item_bool(item_id: int, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"dscription": f"short is {short}"})
    return item


# 定义有多个查询的接口
@app.get('/users/{user_id}/items/{item_id}')
async def get_item_multi(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc": f"Short is {short}"})
    return item