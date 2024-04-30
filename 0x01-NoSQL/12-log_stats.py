#!/usr/bin/env python3
"""This module for task 12."""
from pymongo import MongoClient


def print_logs(NgxClt):
    """
    function that print logs data.
    Args:
        NgxClt: Collection of nginx.
    """
    print('{} logs'.format(NgxClt.count_documents({})))
    print('Methods:')
    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        CountSearch = len(list(NgxClt.find({'method': method})))
        print('\tmethod {}: {}'.format(method, CountSearch))
    CountSearch = len(list(NgxClt.find({'method': 'GET', 'path': '/status'})))
    print('{} status check'.format(CountSearch))


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_logs(client.logs.nginx)
