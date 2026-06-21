#!/usr/bin/env python3
'''Module 12-log_stats'''
from pymongo import MongoClient


if __name__ == "__main__":
    '''Provides some stats about Nginx logs'''

    db = MongoClient("mongodb://127.0.0.1:27017").logs
    mongo_collection = db.nginx


    total_logs = mongo_collection.estimated_document_count()
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
