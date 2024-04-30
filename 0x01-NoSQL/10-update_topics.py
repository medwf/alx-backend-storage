#!/usr/bin/env python3
"""This module for task 10."""
# from pymongo.collection import Collection


def update_topics(mongo_collection, name, topics):
    """
    function that changes all topics of a school document based on the name
    Args:
        mongo_collection: Collection.
        name: (str) will be the school name to update.
        topics: (list) will be the list of topics approached in the school.
    return:
        ...
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
