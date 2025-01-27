# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python


def maskify(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))