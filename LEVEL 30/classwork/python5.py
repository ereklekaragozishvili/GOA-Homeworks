# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

def digitize(n):
    mylist = [int(i) for i in str(n)]
    mylist.reverse()
    return mylist