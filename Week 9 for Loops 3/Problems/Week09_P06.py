def allDistinct(numbers):
    # ADD ADDITIONAL CODE HERE!
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] == numbers[j]:
                return False
    return True


print(allDistinct([1,3,2,5,2,1]))   # False
print(allDistinct([1,0,2,5,3,4]))   # True 


print("==============================================")

def allWithinRange(numbers, lower, upper):
    # ADD ADDITIONAL CODE HERE!
    for i in range(len(numbers)):
        if not (lower <= numbers[i] <= upper):
            return False
    return True


print(allWithinRange([1,0,2,6,3,4], 0,5))   # False
print(allWithinRange([1,0,2,5,3,4], 0,5))   # True 


print("==============================================")

def isPermutation(numbers):
    return allDistinct(numbers) and allWithinRange(numbers, 0, len(numbers)-1)


print(isPermutation([1,3,2,5,2,1]))   # False
print(isPermutation([1,0,2,5,3,4]))   # True
print(isPermutation([1,0,2,6,3,4]))   # False
