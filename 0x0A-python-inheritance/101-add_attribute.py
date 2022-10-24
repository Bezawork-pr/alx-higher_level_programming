#!/usr/bin/python3
"""This file cointains one func"""


def add_attribute(classname, attributename, value):
    """function add_attribute"""
    if type(classname) == str:
        raise TypeError('can\'t add new attribute')
    if type(classname) == int:
        raise TypeError('can\'t add new attribute')
    if type(classname) == list:
        raise TypeError('can\'t add new attribute')
    if type(classname) == tuple:
        raise TypeError('can\'t add new attribute')
    if type(classname) == bool:
        raise TypeError('can\'t add new attribute')
    if type(classname) == dict:
        raise TypeError('can\'t add new attribute')
    setattr(classname, attributename, value)
