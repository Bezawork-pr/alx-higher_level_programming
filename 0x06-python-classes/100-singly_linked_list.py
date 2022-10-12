#!/usr/bin/python3
"""Create a class named Node"""


class Node:
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None and isinstance(next_node, Node) is False:
            raise TypeError("next_node must be a Node object")
        self.data = data
        self.next = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, value):
        self.__next = value


class SinglyLinkedList:
    """Create a class named SinglyLinkedList"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            return
        elif self.head is not None:
            current = self.head
            while current.next is not None:
                if current.data >= value:
                    break
                current = current.next
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            return

    def __str__(self):
        res = ""
        copy = self.head
        reslist = []
        count = 0
        while copy is not None:
            reslist.append(copy.data)
            copy = copy.next
        reslist.sort()
        length = len(reslist)
        while count < length:
            if (count == length - 1):
                res += str(reslist[count])
            else:
                res += str(reslist[count]) + "\n"
            count += 1
        if len(res):
            return res
        else:
            return ""
