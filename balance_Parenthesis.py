"""
In this problem we are demonstrating the use of stack
in real time.

For example say we have to match Parenthesis in any string and validate
balance of Parenthesis.

for example:
(), ()(), [({})] -> balanced parenthesis
{[}], ((, )), {[()}] -> imbalanced parenthesis

"""
# Importing stack module from other file
import stack


# Method which checks match
def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False


def is_valid_parenthesis(paren_string):
    s = stack.Stack()
    index = 0
    is_balanced = True

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]

        if paren in '([{':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()  # top value : '({['
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    return is_balanced


print(is_valid_parenthesis('({[]()[]})'))  # output : True
