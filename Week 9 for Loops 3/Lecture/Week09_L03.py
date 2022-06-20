def isIncreasingSequence(numbers):
    for i in range(len(numbers)-1):
        if not (numbers[i] <= numbers[i+1]):  # numbers[i] > numbers[i+1]
            return False
            
    return True


    
numbers1 = [ 2, 3, 6, 8, 11, 14 ]
numbers2 = [ 2, 3, 6, 8, 7, 14 ]
print(isIncreasingSequence(numbers1))  # output: True
print(isIncreasingSequence(numbers2))  # output: False