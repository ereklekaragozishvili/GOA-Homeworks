# https://www.codewars.com/kata/568d0dd208ee69389d000016

def rental_car_cost(d):
    discount = 0
    if d >= 7:
        discount = 50
    elif d >= 3:
        discount = 20
    return d * 40 - discount