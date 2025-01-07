# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    print(are_you_playing_banjo("Ravi"))  
print(are_you_playing_banjo("Sam"))  
print(are_you_playing_banjo("robert"))  
print(are_you_playing_banjo("David")) 