#!/usr/bin/env python3
'''Module 8-all'''
from pymongo import MongoClient


def list_all(mongo_collection):
    '''Returns a list of all documents in a collection'''
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
