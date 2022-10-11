#!/usr/bin/python3
"""Create a class named Node"""
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, value):
        if value != None or isinstance(value, Node) is False:
            raise TypeError("next_node must be a Node object")

        self.__next = value


class SinglyLinkedList:
    """Create a class named SinglyLinkedList"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        return True


