#!/usr/bin/env python3
"""
cache module
"""
import redis
from typing import Union
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
