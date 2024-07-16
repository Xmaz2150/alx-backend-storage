#!/usr/bin/env python3
"""
schools_by_topic module
"""


def schools_by_topic(mongo_collection, topic):
    """
    gets all schools with specific topic `topic`
    """
    docs = []
    for doc in mongo_collection.find():
        topics = doc.get("topics")
        if topics:
            if topic in topics:
                docs.append(doc)

    return docs
