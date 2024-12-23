# 4) პირველ დავალებაში შექმნილი
# List'იდან გამოიტანეთ პირველი სამი,
#  ბოლო სამი და შუა 4 უარყოფითი ინდექსებით. (slicing)

list1 =[1,2,3,4,5,6,7,8,9,10]

first_three = list1[:3]

last_three  = list1[-3:]

middle_four = list1[-7:-3]

print("პირველი სამი",first_three)

print("ბოლო სამი",last_three)

print("შუა ოთხი", middle_four)
