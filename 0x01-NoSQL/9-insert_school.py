#!/usr/bin/env python3
"""
insert school module
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    """
    d = {}
    for k,v in kwargs.items():
        d[k] = v

    return mongo_collection.insert_one(d).inserted_id
