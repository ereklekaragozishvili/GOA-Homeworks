# 4) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს list'ს და გამოიტანს პირველ 3 რიცხვს

def get_first_three(numbers):
    return numbers[:3]
numbers = [1, 2, 3, 4, 5]
result = get_first_three(numbers)
print(result)  