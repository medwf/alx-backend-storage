#!/usr/bin/env python3
"""This module for task 11"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic
    Args:
        mongo_collection: Collection
        topic: (string) will be topic searched.
    return:
        List(dict) having a specific topic.
    """
    return [doc for doc in mongo_collection.find({
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    })]
