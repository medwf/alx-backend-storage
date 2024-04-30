#!/usr/bin/python3
"""
this module for task 8
"""
from typing import List
from pymongo.collection import Collection 

def list_all(mongo_collection: Collection) -> List[dict]:
    """
    function that lists all documents in a collection.
    Args:
        mongo_collection: Collection
    Return:
        a List of dict.
    """
    return [doc for doc in mongo_collection.find()]
