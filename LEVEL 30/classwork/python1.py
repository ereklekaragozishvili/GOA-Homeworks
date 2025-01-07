# https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python

def basic_op(operation: str, value1: int, value2: int) -> int:
    if operation == "+":
        return value1 + value2
    elif operation == "-":
        return value1 - value2
    elif operation == "*":
        return value1 * value2
    elif operation == "/":
        return value1 / value2
