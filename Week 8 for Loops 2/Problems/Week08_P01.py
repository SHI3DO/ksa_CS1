def countZero(numbers):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            counter += 1

    return counter


print(countZero([0,4,0,-2,4,0]))         # 3
print(countZero([1,0,-2,4,0,0,-7,0,5]))  # 4