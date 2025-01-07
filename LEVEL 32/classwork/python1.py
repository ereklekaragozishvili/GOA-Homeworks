# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    parts = name.split()
    initials = parts[0][0].upper() + '.' + parts[1][0].upper()
    return initials
print(abbrev_name("Sam Harris"))  
print(abbrev_name("patrick feeney"))