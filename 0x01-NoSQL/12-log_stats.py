#!/usr/bin/env python3
"""
provides stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(nginx_logs.count_documents({}), " logs")
    print("methods:")

    for method in methods:
        m_count = nginx_logs.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, m_count))
    status = nginx_logs.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))
