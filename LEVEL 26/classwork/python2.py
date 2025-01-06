# 2) შექმენით ფუნქცია even_or_odd რომელიც
#  მიიღებს რიცხვს პარამეტრად და დააბრუნებს
# #   "Even" თუ ის არის ლუწი, ხოლო "Odd" თუ კენტია

def even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(4))  
print(even_or_odd(7))  
