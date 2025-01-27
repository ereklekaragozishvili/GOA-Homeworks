# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(s):
    counter = 0
    output = ""
    for letter in s:
        output += letter.upper() + letter.lower() * counter + '-'
        counter += 1
    return output[:-1]
