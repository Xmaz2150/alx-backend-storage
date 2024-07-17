#!/usr/bin/env python3
"""
cache module
"""
import redis
from typing import Union, Callable, Optional
from functools import wraps
import uuid


def count_calls(method: Callable) -> Callable:
    """
    decorator to count number times method is called,
    using redis INCR to increment count for method's
    qualified name
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs and outputs for
    `store`
    """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


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

    @count_calls
    @call_history
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
