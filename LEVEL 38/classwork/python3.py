# 3) შექმენით რაიმე list'ი სახელებით და შემდეგ შექმენით list comprehension
#  რომელიც შექმნის სახელების ახალ list'ს სადაც არ იქნება ასო "a" და ყველა string'ს თავში ექნება "#".

names = ["Anna", "John", "Maria", "Alice", "Bob"]  # ორიგინალური სია
filtered_names = [f"#{name}" for name in names if "a" not in name.lower()]
print(filtered_names)
['#John', '#Bob']
