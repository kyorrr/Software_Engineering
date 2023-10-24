import math

def geron(a, b, c):
    p = (a + b + c)/2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

