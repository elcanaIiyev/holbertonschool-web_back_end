#!/usr/bin/env python3
'''Module 11-schools_by_topic'''
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    '''Returns the list of school having a specific topic'''
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({"topics": topic}))
