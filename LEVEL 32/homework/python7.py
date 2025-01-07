#  გააკეთეთ manual_swapcase ფუნქცია

def manual_swapcase(text):
    result = []
    
    for char in text:
        if char.islower():  
            result.append(char.upper())  
        elif char.isupper():  
            result.append(char.lower())  
        else:
            result.append(char)  
    
    return ''.join(result)
print(manual_swapcase("Hello World!"))  
print(manual_swapcase("Python 123"))    
print(manual_swapcase("This Is A Test"))  