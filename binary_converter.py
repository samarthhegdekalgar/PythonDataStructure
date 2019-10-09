""" This module is designed to convert any integer number to
binary using stack """

from stack import Stack


def get_bin(int_number):
    s = Stack()
    bin_number = ''
    while int_number > 0:
        reminder = int_number % 2
        s.push(reminder)
        int_number = int_number // 2
    while not s.is_empty():
        bin_number += str(s.pop())
    return bin_number


print(get_bin(2421234343))  # output : 10010000010100010001101010100111
