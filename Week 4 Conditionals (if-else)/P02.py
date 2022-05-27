def countZeros(n1, n2, n3, n4, n5):
    counter = 0

    if n1 == 0:
        counter = counter + 1

    if n2 == 0:
        counter = counter + 1

    if n3 == 0:
        counter = counter + 1

    if n4 == 0:
        counter = counter + 1

    if n5 == 0:
        counter = counter + 1

    return counter
    # ADD ADDITIONAL CODE HERE!


print(countZeros(1, 0, 3, 0, 0))  # 3
print(countZeros(0, 2, 2, 0, 4))  # 2
print(countZeros(1, 2, 3, 0, 4))  # 1
print(countZeros(1, 2, 3, 5, 4))  # 0
