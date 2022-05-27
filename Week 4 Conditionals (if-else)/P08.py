def f(a, b, c, x):
    return a * x ** 2 + b * x + c


def minX(a, b, c):
    x0 = int(-b / (2 * a))
    if f(a, b, c, x0) <= f(a, b, c, x0 + 1):
        return x0
    else:
        return x0+1
    # ADD ADDITIONAL CODE HERE!


print(minX(1, -9, 2))  # 4
print(minX(9, -5, 0))  # 0
print(minX(9, -15, 0))  # 1
print(minX(7, -13, 3))  # 1
