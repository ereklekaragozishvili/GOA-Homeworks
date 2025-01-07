#  https://www.codewars.com/kata/583710ccaa6717322c000105/train/python

def simple_multiplication(number):
    if number % 2 == 0: 
        return number * 8
    else:  
        return number * 9
print(simple_multiplication(4))   
print(simple_multiplication(7))   
print(simple_multiplication(10)) 
print(simple_multiplication(3))   
