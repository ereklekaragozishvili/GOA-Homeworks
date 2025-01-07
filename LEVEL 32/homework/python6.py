#  გააკეთეთ manual_find ფუნქცია

def manual_find(text, substring):
  
    if not substring:
        return 0
    
    for i in range(len(text) - len(substring) + 1):
        if text[i:i+len(substring)] == substring:
            return i
    return -1
print(manual_find("hello world", "world"))  
print(manual_find("hello world", "python")) 
print(manual_find("hello world", ""))       