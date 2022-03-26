"""
定义查询参数接口，函数的参数存放在请求 url 中，是 url 的一部分
1. 请求 url 实际为：http://127.0.0.1:8000/items/?skip=0&limit=10
2. 该类型参数并不是 url 中固定的部分，因此是多选，并且可以有默认值，可以用 Optional 声明参数
3. fastapi 会对类型声明为 bool 的参数自动转换为 True or False
4. 可以通过给参数设置默认值来表明该参数是一个可选参数，反之则为必选参数
"""

from fastapi import FastAPI, Query

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 定义两个查询参数的接口
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


from typing import Optional, List


# 定义可选参数的接口
@app.get('/items/{item_id}')
async def get_item(item_id: int, q: Optional[str] = None):  # 参数 q 类型为 str，可选，默认 None
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 参数 q 类型为 str，可选，默认 None, 最短 3 个字符，最长 10 个字符，且必需数字开头
@app.get('/items1/{item_id}')
async def get_item_check(item_id: int, q: Optional[str] = Query(None, min_length=3, max_length=10, regex="^12345")):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 参数 q 类型为 str 类型的列表，可选，默认 None,
@app.get('/items2/{item_id}')
async def get_item_multi(item_id: int, q: Optional[List[str]] = Query(None)):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 参数 q 类型为 str 类型的列表，可选，默认 None，并请求 url 中使用别名 item-query 而不是 q
# 比如：http://127.0.0.1:8000/items3/1?item-query=string
@app.get('/items3/{item_id}')
async def get_item_alias(item_id: int, q: Optional[List[str]] = Query(None, alias="item-query")):
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