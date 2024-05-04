#!/usr/bin/env python3
"""
This module for redis exercise
"""
import redis
import uuid
from typing import Union, Callable
# print(dir(redis))


class Cache:
    """
    class redis
    """

    def __init__(self):
        """DOC"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store data using random id as string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Union[Callable, None]
            ) -> Union[str, bytes, int, float]:
        """
        a methods that get a value from redis storage
        """
        value = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_str(self, key: str) -> str:
        """
        a methods that get a string value from redis storage
        """
        return self._redis.get(key, lambda v: str(v))

    def get_int(self, key: str) -> int:
        """
        a methods that get an integer from redis storage
        """
        return self._redis.get(key, lambda v: int(v))
