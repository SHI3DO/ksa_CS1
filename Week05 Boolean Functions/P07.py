def intersect(a, b, c, d, e, f):
    k = (a - d) ** 2 + (b - e) ** 2
    return (c + f) ** 2 > k > (c - f) ** 2


# ADD FUNCTION HERE!


print(intersect(1, 1, 3, 5, 4, 2))  # False
print(intersect(1, 1, 3, 4, 3, 2))  # True
print(intersect(1, 1, 3, 2, 1, 2))  # False
