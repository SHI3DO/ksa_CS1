def digit(n, k):
    # ADD ADDITIONAL CODE HERE!
    n = 1 / n
    return int(n * 10 ** k) % 10


print(digit(47, 5))  # 7
print(digit(47, 6))  # 6
print(digit(47, 7))  # 5
print(digit(47, 8))  # 9
print(digit(47, 9))  # 5
