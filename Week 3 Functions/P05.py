def f(a, b, c, x):
    return a * x ** 2 + b * x + c


def minValue(a, b, c):
    # ADD ADDITIONAL CODE HERE!
    x = -b / (2 * a)
    return f(a, b, c, x)


print(minValue(1, 5, 10))  # 3.75
print(minValue(1, -5, 10))  # 3.75
print(minValue(3, 7, 5))  # 0.9166666666666661
