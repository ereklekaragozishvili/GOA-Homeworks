#  https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python


def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)