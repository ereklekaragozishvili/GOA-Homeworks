#  შექმენით manual_max ფუნქცია

def manual_max(iterable):
    if not iterable:
        raise ValueError("The iterable cannot be empty")
    
    max_value = iterable[0]  
    for item in iterable:
        if item > max_value:  
            max_value = item
    return max_value


numbers = [3, 5, 7, 2, 8]
print(manual_max(numbers))  
