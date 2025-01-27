# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python


def high_and_low(numbers):
    n = sorted([int(x) for x in numbers.split()])
    return '{} {}'.format(n[-1], n[0])