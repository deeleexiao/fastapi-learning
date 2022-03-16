"""
fastapi：是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+ 并基于标准的 Python 类型提示。
FastApi：是 fastapi 的实例类，直接从 Starlette 继承
Starlette：Starlette 是一个轻量级的 ASGI 框架和工具包，特别适合用来构建高性能的 asyncio 服务
ASGI：Async Server Gateway Interface，异步服务网关接口，旨在支持异步的 Python Web 服务器、框架和应用程序之间的标准接口，同时向后兼容 WAGI
WSGI：Web Server Gateway Interface，web 服务网关接口，属于 web 应用的底层的通讯标准接口，让我们不必关注 TCP、HTTP 请求等细节
Uvicorn：是基于 uvloop 和 httptools 构建的非常快速的 ASGI 服务器
uvloop：用于替换标准库 asyncio 中的事件循环，使用 Cython 实现，它非常快，可以使 asyncio 的速度提高 2-4 倍
asyncio：Python 异步程序标准库，用来支持 python 的异步代码

fastapi应用：
1. 需要使用 unicorn 等 ASGI 服务器启动应用
2. 自带完善的 OpenAPI 文档（Swagger）http://127.0.0.1:8000 以及 http://127.0.0.1:8000/redoc
3. http://127.0.0.1:8000/openapi.json OpenAPI 的实际数据
"""


from fastapi import FastAPI


app = FastAPI()


# 第一个 fastapi 接口
@app.get('/')
async def root():
    return {"message": "Hello World"}


# post 方法接口
@app.post('/post-i')
def post_i():
    return {"msg": "hello, post"}


# put 方法接口
@app.put('/put-i')
async def put_i():
    return {"msg": "hello, put"}


# delete 方法接口
@app.delete('/delete-i')
def delete_i():
    return {"msg": "hello, delete"}