#!/usr/bin/env python3
"""
This module for redis exercise
"""
import redis
import uuid
# print(dir(redis))


class Cache:
    """
    class redis
    """

    def __init__(self):
        """DOC"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
        store data using random id as string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
