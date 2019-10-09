"""
This module is designed to demonstrate the
implementations of stack in python.

Stack : A stack is an array or list structure of
function calls and parameters used in modern computer
programming and CPU architecture.

"""


class Stack:
    def __init__(self):
        self.items = []  # Stack holder which stores all element

    def push(self, item):  # This method is used to push element into stack
        self.items.append(item)

    def pop(self):  # This method is used to pop element from stack
        if not self.is_empty():
            return self.items.pop()
        else:
            return 'Stack is empty!'

    def get_stack(self):  # This method returns all element of stack
        return self.items

    def peek(self):  # This method returns top element of stack
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack is empty!'

    def is_empty(self):  # This method helps to check stack is empty or not returns TRUE or FALSE
        return self.items == []

