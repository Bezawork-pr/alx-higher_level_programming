#!/usr/bin/python3
"""
This file contains class Base
"""
import json
import os


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiate"""
        if id is not None:
            self.id = id
        elif id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Change from object to json string"""
        if list_dictionaries is None:
            return "[]"
        for i in range(len(list_dictionaries)):
            list_dictionaries[i] = dict(reversed(list(
                list_dictionaries[i].items())))
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json string in file"""
        my_list = []
        if list_objs is None:
            with open(file_name, "a", encoding="utf-8") as rw:
                json_string = cls.to_json_string(my_list)
                rw.write(json_string)
        else:
            file_name = cls.__name__ + ".json"
            if os.path.exists(file_name) is True:
                with open(file_name, "r", encoding="utf-8") as copy:
                    read_copy = copy.read()
                    if len(read_copy) != 0:
                        previous_list = json.loads(read_copy)
                        for i in range(len(previous_list)):
                            my_list.append(previous_list[i])
            for i in range(len(list_objs)):
                my_list.append(list_objs[i].to_dictionary())
                json_string = cls.to_json_string(my_list)
            with open(file_name, "w+", encoding="utf-8") as w:
                w.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Get object from json string"""
        to_list = []
        if json_string is None:
            return to_list
        to_list = json.loads(json_string)
        return to_list
    
    @classmethod
    def create(cls, **dictionary):
        """Create dummy instance and update using the update function"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

