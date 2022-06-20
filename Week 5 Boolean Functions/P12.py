def intersect(x1, y1, l1, x2, y2, l2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    c = abs(l1 - l2) / 2
    d = (l1 + l2) / 2
    return c < a < d and c < b < d


print(intersect(1, 1, 4, 4, 3, 4))  # True
print(intersect(1, 1, 4, 3, 6, 4))  # False
print(intersect(1, 1, 4, 2, 3, 2))  # False
print(intersect(1, 1, 4, 2, 2, 2))  # False
print(intersect(1, 1, 4, 2, 1, 2))  # False
print(intersect(1, 1, 4, 4, 3, 2))  # False
