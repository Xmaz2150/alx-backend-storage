#!/usr/bin/env python3
"""
cache module
"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """
    Cache class
    """
    _redis = None

    def __init__(self):
        """
        initializer
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates random key and stores `data` using key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[any]:
        """
        retrieve value from server by key,
        optionally apply transformation function `fn` to the retrieved value.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        retrieves string value from server by key using `get`
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        retrieves int value from server by key using `get`
        """
        return self.get(key, fn=int)
