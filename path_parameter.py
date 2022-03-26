"""
fastapi 接口路径参数定义
1. 不同的接口，所定义的路径，应是不同的，否则会被当成一个接口，比如：/users/me 和 /users/{user_id}，me 会被作为 user_id 请求 /users
"""

from fastapi import FastAPI, Path

app = FastAPI()


# 路径参数作为函数的入参
@app.get('/items/{item_id}')
async def get_item(item_id):
    return {"item_id": item_id}


# 有类型的路径参数，并且返回结果类型自动转换为声明的参数类型，如果入参类型不符合，默认返回 fastapi 的类型校验结果（可重写该类返回自定义结果）
@app.get('/item-int/{item_id_int}')
async def get_item_int(item_id_int: int):
    return {"item_id_str": item_id_int}


from enum import Enum


# 路径参数是一个枚举值，定义一个枚举类，并给路径参数声明
class ModelName(str, Enum):

    firstname = 'firstnme'
    lastname = 'lastname'
    noname = 'noname'


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == model_name.firstname:
        return {"model_name": model_name, "msg": "This is firstname"}
    elif model_name == model_name.lastname:
        return {"model_name": model_name, "msg": "This is lastname"}
    else:
        return {"model_name": model_name, "msg": "noname"}


# 对参数排序的技巧
# 将带有「默认值」的参数放在没有「默认值」的参数之前，Python 将会报错
# Python 不会对该 * 做任何事情，但是它将知道之后的所有参数都应作为关键字参数（键值对），也被称为 kwargs，来调用。即使它们没有默认值
@app.get('/item/{item_id_int}')
async def get_item_int1(*, q: str, item_id_int: int = Path(...)):
    return {"item_id_str": item_id_int,
            "q": q}


# 校验参数大小，可以使用 Path、Query
# 比如 大于 1，小于 10
@app.get('/item2/{item_id_int}')
async def get_item_int2(*, q: str, item_id_int: int = Path(..., ge=1, lt=10)):
    return {"item_id_str": item_id_int,
            "q": q}
