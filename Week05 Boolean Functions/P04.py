# ADD FUNCTION HERE!
def triangle(a, b, c):
    sum = a + b + c
    return max(a, b, c) < sum - max(a, b, c)


print(triangle(3, 4, 5))  # True
print(triangle(1, 5, 2))  # False
print(triangle(3, 1, 1))  # False
