def inSecondQuadrant(x, y):
    # ADD ADDITIONAL CODE HERE!
    return x < 0 and y > 0


print(type(inSecondQuadrant(0, 0)))  # <class 'bool'>
print(inSecondQuadrant(-1, 2))  # True
print(inSecondQuadrant(-1, -2))  # False
print(inSecondQuadrant(1, -2))  # False
print(inSecondQuadrant(-1, 0))  # False

print("==============================================")


def exactlyTwoSecondQuadrant(x1, y1, x2, y2, x3, y3):
    # ADD ADDITIONAL CODE HERE!
    counter = 0

    if inSecondQuadrant(x1, y1):
        counter = counter + 1

    if inSecondQuadrant(x2, y2):
        counter = counter + 1

    if inSecondQuadrant(x3, y3):
        counter = counter + 1

    return counter == 2


print(exactlyTwoSecondQuadrant(-1, 2, 2, 1, -2, 1))  # True
print(exactlyTwoSecondQuadrant(1, 2, -2, 1, -3, 3))  # True
print(exactlyTwoSecondQuadrant(1, 2, -2, -1, -2, 1))  # False
print(exactlyTwoSecondQuadrant(-1, 2, -2, 1, -2, 2))  # False
print(exactlyTwoSecondQuadrant(1, 2, -2, -1, 2, -2))  # False
