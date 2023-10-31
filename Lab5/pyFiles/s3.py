import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def area(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

one_max = max(one)
one_min = min(one)
two_max = max(two)
two_min = min(two)
three_max = max(three)
three_min = min(three)

max_list = [one_max, two_max, three_max]
min_list = [one_min, two_min, three_min]

max_triangle = area(*max_list)
min_triangle = area(*min_list)

print("Макс. треугольник: ", round(max_triangle))
print("Мин. треугольник: ", round(min_triangle))