"""
定义接口的请求体
1. 使用 Pydantic 类型来声明请求体
2. 声明请求体，并从 pydantic 继承 BaseModel
3. 给接口的请求参数声明为自定义的请求体类型，比如：payload: Item
"""

from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Body

app = FastAPI()


class Item(BaseModel):
    """
    定义 item 请求体
    """
    name: str
    description: Optional[str] = None  # 参数可选，并赋予默认值
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    """
    定义 User 请求体
    """
    firname: str
    lastname: str


@app.post('/item/')
async def item(payload: Item):
    return payload


# 多个自定义请求体，以及单独的请求参数
@app.post('/items/')
async def items(payload: Item, userinfo: User, single: int = Body(...)):
    return {"item": payload, "user": userinfo, "single": single}


# 多个自定义请求体，以及单独的请求参数，且有路径参数，Body 将参数转换为 k-v
@app.post('/items/{item_id}/')
async def items1(item_id: int, payload: Item, userinfo: User, single: int = Body(...)):
    return {"item_id": item_id, "item": payload, "user": userinfo, "single": single}
