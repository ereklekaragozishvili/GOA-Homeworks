# https://www.codewars.com/kata/515e271a311df0350d00000f

def square_sum(numbers):
    result = []
    for sqr in numbers:
        result.append(sqr ** 2)
    return sum(result)