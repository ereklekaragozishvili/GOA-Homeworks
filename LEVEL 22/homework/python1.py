# 2) შექმენით ფუნქცია რომელიც დააბრუნებს
#  "You got discount" თუ მომხმარებელი არის არასრულწლოვანი, სხვა შემთხვევაში დააბრუნებს "You didn't get discount"


def function(age):
    if age < 18:
        return "You got discount"
    else:
        return "You didn't get discount"

# print(function (18)) 

# print(function(11))