def somePositive(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 0:
            return True
    return False

    
def allPositive(numbers):
    for i in range(len(numbers)):
        if not (numbers[i] > 0): # numbers[i] <= 0
            return False
    return True

    

num1 = [1, 3, 2, 5, 2, 1]
num2 = [-1,-3,-2,-5,-2,-1]
num3 = [-1,-3,-2, 5,-2, 1]
print(somePositive(num1), allPositive(num1))
print(somePositive(num2), allPositive(num2))
print(somePositive(num3), allPositive(num3))