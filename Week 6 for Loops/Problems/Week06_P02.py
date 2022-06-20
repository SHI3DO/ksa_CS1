def sumNumbers(a,b):
    sum = 0
    # ADD ADDITIONAL CODE HERE!
    for i in range(a,b+1):
        sum += i

    return sum


print(sumNumbers(5,10))    # 45
print(sumNumbers(15,100))  # 4945