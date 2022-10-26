#!/usr/bin/python3
"""
This file contains class Student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        my_dict = {}
        if attrs is None:
            return dict(reversed(list(self.__dict__.items())))
        for i in range(len(attrs)):
            if attrs[i] == "first_name":
                my_dict["first_name"] = self.first_name
            elif attrs[i] == "last_name":
                my_dict["last_name"] = self.last_name
            elif attrs[i] == "age":
                my_dict["age"] = self.age
            else:
                pass
        dict_reversed = dict(reversed(list(my_dict.items())))
        return dict_reversed

    def reload_from_json(self, json):
        """Load data from file"""
        if json.get("first_name") is not None:
            self.first_name = json["first_name"]
        if json.get("last_name") is not None:
            self.last_name = json["last_name"]
        if json.get("age") is not None:
            self.age = json["age"]
        return self.__dict__
