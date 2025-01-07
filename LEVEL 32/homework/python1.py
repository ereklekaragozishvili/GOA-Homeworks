#  https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python

def find_average(nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)
