import math as m

def score(x, y):
    d = distance(x, y)
    if d <= 1:
        return 10
    elif d <= 5:
        return 5
    elif d <= 10:
        return 1
    return 0

def distance(x, y):
    return m.sqrt(pow(x, 2) + pow(y, 2))
