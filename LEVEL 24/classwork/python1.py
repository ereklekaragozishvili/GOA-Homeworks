# 1) დღეს რომელი ფუნქციები და მეთოდები ვისწავლეთ, გატესტეთ ყველა: len(), .append(), .insert(), .pop(), .remove()

# 1. len()
my_list = [1, 2, 3, 4, 5]
print("len():", len(my_list)) 

# 2. .append()
list = [1,2,3,4,5]
list.append(6)
print(".append():", list) 

# 3. .insert()
my_list.insert(2, 10) 
print(".insert():", my_list)

# 4. .pop()
popped_value = my_list.pop(3)  
print(".pop():", popped_value) 
print("After .pop():", my_list) 

# 5. .remove()
my_list.remove(10)  
print(".remove():", my_list) 
