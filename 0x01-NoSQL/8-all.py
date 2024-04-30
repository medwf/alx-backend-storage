#!/usr/bin/env python3
"""
this module for task 8
"""
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List[dict]:
    """
    function that lists all documents in a collection.
    Args:
        mongo_collection: Collection
    Return:
        a List of dict.
    """
    return [doc for doc in mongo_collection.find()]
