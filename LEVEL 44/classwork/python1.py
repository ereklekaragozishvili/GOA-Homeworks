# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

def friend(x):
    #Code
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

