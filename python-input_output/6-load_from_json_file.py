#!/usr/bin/python3
'''a function that creates an object from a JSON file'''


import json


def load_from_json_file(filename):
    '''Function that does not work'''
    with open(filename, 'r') as f:
        return json.load(f)
