#!/usr/bin/python3
"""
This file contains class Base
class Base gives id number
if no id is provided by the user
class Base generates for the instance
"""
import json
import os
import csv
import turtle


class Base:
    """class Base has both static and class method
    that has functions like drawing Rectangles and
    squares, instantiate the objects
    change from object to json string, save to json file, get
    object from json string, create dummy instances and
    update the attributes, load from json file, save to json file,
    load from csv file and read to csv file"""
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
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            with open(file_name, "w+", encoding="utf-8") as w:
                json_string = cls.to_json_string(my_list)
                w.write(json_string)
                return
        else:
            if os.path.exists(file_name) is False:
                with open(file_name, "w+", encoding="utf-8") as createfile:
                    json_string = cls.to_json_string(my_list)
                    createfile.write(json_string)
            with open(file_name, "r", encoding="utf-8") as copy:
                read_copy = copy.read()
                if len(read_copy) != 0:
                    previous_list = json.loads(read_copy)
                    for i in range(len(previous_list)):
                        my_list.append(previous_list[i])
                for i in range(len(list_objs)):
                    my_list.append(list_objs[i].to_dictionary())
                    json_string = cls.to_json_string(my_list)
                with open(file_name, "w+", encoding="utf-8") as wr:
                    wr.write(json_string)

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

    @classmethod
    def load_from_file(cls):
        """Load from json file"""
        my_list = []
        my_instances = []
        file_name = cls.__name__ + ".json"
        if os.path.exists(file_name) is True:
            with open(file_name, "r", encoding="utf-8") as copy:
                read_copy = copy.read()
                my_list = cls.from_json_string(read_copy)
            for i in range(len(my_list)):
                my_instances.append(cls.create(**my_list[i]))
            return my_instances
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to csv file"""
        file_name = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
            my_list = []
            for elem in list_objs:
                my_dict = {}
                my_dict['id'] = elem.id
                my_dict['width'] = elem.width
                my_dict['height'] = elem.height
                my_dict['x'] = elem.x
                my_dict['y'] = elem.y
                my_list.append(my_dict)
        else:
            fieldnames = ["id", "size", "x", "y"]
            my_list = []
            for elem in list_objs:
                my_dict = {}
                my_dict['id'] = elem.id
                my_dict['size'] = elem.size
                my_dict['x'] = elem.x
                my_dict['y'] = elem.y
                my_list.append(my_dict)
        with open(file_name, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in my_list:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Load from csv file"""
        file_name = cls.__name__ + ".csv"
        loaded = []
        my_dict = {}
        with open(file_name, encoding="utf-8") as r:
            reader = csv.DictReader(r)
            for elem in reader:
                if cls.__name__ == "Rectangle":
                    my_dict['id'] = int(elem['id'])
                    my_dict['width'] = int(elem['width'])
                    my_dict['height'] = int(elem['height'])
                    my_dict['x'] = int(elem['x'])
                    my_dict['y'] = int(elem['y'])
                if cls.__name__ == "Square":
                    my_dict['id'] = int(elem['id'])
                    my_dict['size'] = int(elem['size'])
                    my_dict['x'] = int(elem['x'])
                    my_dict['y'] = int(elem['y'])
                loaded.append(cls.create(**my_dict))
        return loaded

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw using turtle"""
        for elem in list_rectangles:
            my_screen = turtle.Screen()
            my_screen.setup(500, 500)
            my_screen.bgcolor("blue")
            my_drawing = turtle.Turtle()
            my_drawing.goto(elem.x, elem.y)
            my_drawing.forward(elem.width)
            my_drawing.left(90)
            my_drawing.forward(elem.height)
            my_drawing.right(90)
            my_drawing.forward(elem.width)
            my_drawing.right(90)
            my_drawing.forward(elem.height)
            turtle.done()

        for elem in list_squares:
            my_screen = turtle.Screen()
            my_screen.setup(500, 500)
            my_screen.bgcolor("blue")
            my_square = turtle.Turtle()
            my_square.goto(elem.x, elem.y)
            my_square.forward(elem.size)
            my_square.left(90)
            my_square.forward(elem.size)
            my_square.right(90)
            my_square.forward(elem.size)
            my_square.right(90)
            my_square.forward(elem.size)
            turtle.done()
