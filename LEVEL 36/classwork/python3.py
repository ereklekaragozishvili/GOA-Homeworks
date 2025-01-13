# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

def count_sheep(n):
    s = ""
    i = 1
    while i <= n:
        s += str(i)+" sheep..."
        i += 1
    return s