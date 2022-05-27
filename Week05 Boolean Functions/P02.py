def withinInterval(lower, upper, n):
    # ADD ADDITIONAL CODE HERE!
    return lower <= n <= upper


print(type(withinInterval(1, 5, 0)))  # <class 'bool'>
print(withinInterval(1, 5, 0))  # False
print(withinInterval(1, 5, 1))  # True
print(withinInterval(1, 5, 3))  # True
print(withinInterval(1, 5, 5))  # True
print(withinInterval(1, 5, 6))  # False

print("==============================================")


def exactlyThreeWithinInterval(lower, upper, n1, n2, n3, n4, n5):
    # ADD ADDITIONAL CODE HERE!
    counter = 0

    if withinInterval(lower, upper, n1):
        counter = counter + 1
    if withinInterval(lower, upper, n2):
        counter = counter + 1
    if withinInterval(lower, upper, n3):
        counter = counter + 1
    if withinInterval(lower, upper, n4):
        counter = counter + 1
    if withinInterval(lower, upper, n5):
        counter = counter + 1

    return counter == 3


print(exactlyThreeWithinInterval(1, 5, 1, 0, 6, 5, 3))  # True
print(exactlyThreeWithinInterval(1, 5, 6, 1, 0, 3, 5))  # True
print(exactlyThreeWithinInterval(1, 5, 6, 1, 0, 7, 2))  # False
print(exactlyThreeWithinInterval(1, 5, 6, 7, 0, 1, 2))  # False
