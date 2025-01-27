# https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python

def area_or_perimeter(l , w):
    if l == w:
        tot = l * w
    else:
        tot = l * 2 + w * 2
    return tot