# ADD FUNCTION HERE!
def acuteAngled(x1, y1, x2, y2, x3, y3):
    a = (x2 - x1) ** 2 + (y2 - y1) ** 2
    b = (x3 - x2) ** 2 + (y3 - y2) ** 2
    c = (x1 - x3) ** 2 + (y1 - y3) ** 2

    return max(a, b, c) < a + b + c - max(a, b, c)


print(acuteAngled(1, 2, 4, 3, 2, 7))  # True
print(acuteAngled(1, 2, 4, 2, 5, 4))  # False
print(acuteAngled(1, 2, 4, 2, 4, 3))  # False
