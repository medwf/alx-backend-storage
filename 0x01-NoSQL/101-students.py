#!/usr/bin/env python3
"""this module for task 101"""


def top_students(mongo_collection):
    """
    function that return all students stored by AVG score.
    Args:
        mongo_collection: Collection
    return:
        list[dict] of all students.
    """
    return mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
