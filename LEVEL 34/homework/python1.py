# https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python


def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)