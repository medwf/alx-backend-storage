#!/usr/bin/env python3
"""
This module for redis exercise
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps
# print(dir(redis))


def count_calls(method: Callable) -> Callable:
    """
    implement a system to count how many times
        methods of the Cache class are called.
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Invokes the given method after incrementing its call counter.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


class Cache:
    """
    class redis
    """

    def __init__(self):
        """DOC"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store data using random id as string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        a methods that get a value from redis storage
        """
        value = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_str(self, value: str) -> str:
        """
        a methods that get a string value from redis storage
        """
        return self._redis.get(value, lambda v: str(v))

    def get_int(self, value: str) -> int:
        """
        a methods that get an integer from redis storage
        """
        return self._redis.get(value, lambda v: int(v))
