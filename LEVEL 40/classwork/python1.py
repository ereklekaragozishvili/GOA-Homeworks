# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python


def getCount(s):
    return sum(c in 'aeiou' for c in s)