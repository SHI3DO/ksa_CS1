def quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return 0

        else:
            return 1

    else:
        D = b ** 2 - 4 * a * c
        if D > 0:
            return 2
        elif D < 0:
            return 0
        else:
            return 1
        # ADD ADDITIONAL CODE HERE!


print(quadratic(0, 0, 1))  # 0
print(quadratic(0, 1, 1))  # 1
print(quadratic(1, -2, 1))  # 1
print(quadratic(1, 1, 1))  # 0
print(quadratic(1, -4, 1))  # 2
