#!/usr/bin/env python3
"""This module for task 9."""
# from pymongo.collection import Collection


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: Collection.
        kwargs: dict of key value.
    return:
        a new _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
