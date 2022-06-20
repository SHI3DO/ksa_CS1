def rightAngled(x1, y1, x2, y2, x3, y3):
    # ADD ADDITIONAL CODE HERE!
    a = (x2 - x1) ** 2 + (y2 - y1) ** 2
    b = (x3 - x2) ** 2 + (y3 - y2) ** 2
    c = (x1 - x3) ** 2 + (y1 - y3) ** 2

    return max(a, b, c) == a + b + c - max(a, b, c)


print(rightAngled(1, 1, 5, 2, -1, 9))  # True
print(rightAngled(1, 2, 4, 2, 5, 4))  # False
print(rightAngled(1, 2, 4, 2, 4, 3))  # True
