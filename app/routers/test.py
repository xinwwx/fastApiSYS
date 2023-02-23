#!usr/bin/env python
# -*- coding:utf-8 _*-
from fastapi import APIRouter, Depends, HTTPException


# 属于该模块的路由
router = APIRouter(
    # 这里配置的 tags、dependencies、responses 对这个模块的内的所有路径操作都生效
    # 路径前缀，该模块下所有路径操作的前缀
    prefix="/test",
    # 标签
    tags=["test"],
    # 依赖项
    # 响应
    # responses={404: {"description": "users Not found"}}
)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}