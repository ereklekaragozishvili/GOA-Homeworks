#  https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python



def openOrSenior(data):
    # Hmmm.. Where to start?
    ret = []
    for datum in data:
        age, handicap = datum
        if age >= 55 and handicap > 7:
            ret.append('Senior')
        else:
            ret.append('Open')
    return ret