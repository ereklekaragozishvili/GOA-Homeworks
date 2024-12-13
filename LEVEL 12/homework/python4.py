# 5) შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ ისევ 10 მაგალითი წინა დავალებების მსგავსად

# 1. (5 > 3) and (2 < 4)
# Result: True (5 > 3 is True, 2 < 4 is True, True and True is True)
print((5 > 3) and (2 < 4))

# 2. (10 == 10) or (3 > 7)
# Result: True (10 == 10 is True, 3 > 7 is False, True or False is True)
print((10 == 10) or (3 > 7))

# 3. (4 != 4) and (7 <= 8)
# Result: False (4 != 4 is False, 7 <= 8 is True, False and True is False)
print((4 != 4) and (7 <= 8))

# 4. (8 >= 8) or (5 < 2)
# Result: True (8 >= 8 is True, 5 < 2 is False, True or False is True)
print((8 >= 8) or (5 < 2))

# 5. not (3 == 3) and (2 > 1)
# Result: False (not (3 == 3) is False, 2 > 1 is True, False and True is False)
print(not (3 == 3) and (2 > 1))

# 6. (6 < 7) or (not (9 != 9))
# Result: True (6 < 7 is True, not (9 != 9) is True, True or True is True)
print((6 < 7) or (not (9 != 9)))

# 7. ((5 > 2) and (3 < 8)) or (7 == 6)
# Result: True ((5 > 2 and 3 < 8) is True, 7 == 6 is False, True or False is True)
print(((5 > 2) and (3 < 8)) or (7 == 6))

# 8. ((2 + 3) == 5) and ((10 - 2) > 5)
# Result: True ((2 + 3) == 5 is True, (10 - 2) > 5 is True, True and True is True)
print(((2 + 3) == 5) and ((10 - 2) > 5))

# 9. ((3 * 2) >= 6) or ((4 / 2) < 1)
# Result: True ((3 * 2) >= 6 is True, (4 / 2) < 1 is False, True or False is True)
print(((3 * 2) >= 6) or ((4 / 2) < 1))

# 10. not ((5 != 5) or (8 < 3))
# Result: True (5 != 5 is False, 8 < 3 is False, False or False is False, not False is True)
print(not ((5 != 5) or (8 < 3)))
