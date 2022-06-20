def countRange(numbers, lower, upper):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    for i in range(len(numbers)):
        if lower <= numbers[i] <= upper:
            counter += 1
    return counter


print(countRange([0,6,2,1,3,4,7], 2,5))           # 3
print(countRange([8,9,10,2,4,5,9,7,2,3,7], 3,7))  # 5
