# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python


def nb_year(p0, percent, aug, p):
    # p0 - начальное население, percent - процент добавления, aug - пребывающие каждый год, p - что нужно превзойти
    per = percent/100
    pn = p0
    i = 0
    while pn < p:
        i = i + 1
        pn = int(pn + pn * per + aug)
        
    return i