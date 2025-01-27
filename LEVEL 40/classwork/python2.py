#  https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python


def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s