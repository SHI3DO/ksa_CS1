def isosceles(x1, y1, x2, y2, x3, y3):
    # ADD ADDITIONAL CODE HERE!
    lengthA = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    lengthB = ((x1-x3)**2 + (y1-y3)**2) ** 0.5
    lengthC = ((x2-x3)**2 + (y2-y3)**2) ** 0.5

    if lengthA == lengthB or lengthA == lengthC or lengthB == lengthC:
        return True

    return False


print(isosceles(1, 1, 2, 5, 3, 1))  # True
print(isosceles(2, 5, 3, 1, 1, 1))  # True
print(isosceles(3, 1, 1, 1, 2, 5))  # True
print(isosceles(1, 1, 1, 3, 3, 2))  # True
print(isosceles(1, 1, 1, 3, 2, 2))  # True
print(isosceles(1, 1, 1, 9, 2, 5))  # True
print(isosceles(1, 1, 2, 5, 3, 2))  # False
print(isosceles(1, 1, 2, 5, 3, 5))  # False
print(isosceles(1, 1, 2, 5, 3, 6))  # False
print(isosceles(2, 5, 3, 2, 1, 1))  # False
