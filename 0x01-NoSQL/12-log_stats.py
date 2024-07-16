#!/usr/bin/env python3
"""
provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

def server_stats(mongo_collection):
    """
    computes stats from collection
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(mongo_collection.count_documents({}), "logs")
    print("Methods:")

    for method in methods:
        m_count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, m_count))
    status = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    nginx_logs = db.nginx
    
    server_stats(nginx_logs)
