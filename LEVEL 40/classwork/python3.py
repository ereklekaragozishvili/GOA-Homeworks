# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python


def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)