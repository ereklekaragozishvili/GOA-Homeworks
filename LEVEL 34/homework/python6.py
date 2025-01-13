#  შექმენით manual_min ფუნქცია

def manual_min(numbers):
    if not numbers:
        raise ValueError("The list is empty")  
    
    min_value = numbers[0]  
    for num in numbers:
        if num < min_value:
            min_value = num  
    return min_value
numbers = [3, 1, 4, 1, 5, 9, -2]
print(manual_min(numbers)) 

print(manual_min([10, 20, 30]))  

print(manual_min([]))  