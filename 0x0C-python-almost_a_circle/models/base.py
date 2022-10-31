#!/usr/bin/python3
"""
This file contains class Base
"""
import json
import os
import csv
import turtle

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
        if os.path.exists(file_name) is False:
            with open(file_name, "w+", encoding="utf-8") as createfile:
                pass
        with open(file_name, "a", encoding="utf-8") as r:
            csv_writer = csv.writer(r)
            csv_writer.writerow(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Load from csv file"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            for i in csv_reader:
                return i

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

