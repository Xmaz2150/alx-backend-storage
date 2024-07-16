#!/usr/bin/env python3
"""
list_all module
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
