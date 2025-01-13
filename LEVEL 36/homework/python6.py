

def is_in(element, collection):
    for item in collection:
        if item == element:
            return True
    return False


print(is_in(3, [1, 2, 3, 4]))  
print(is_in('a', 'banana'))    
print(is_in(5, [1, 2, 3, 4]))  
