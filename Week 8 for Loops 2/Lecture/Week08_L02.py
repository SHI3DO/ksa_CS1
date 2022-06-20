def countNumber(numbers, k):
    counter = 0
    for i in range(len(numbers)):
        if numbers[i] == k:
            counter += 1
            
    return counter


    
num = [ 1, 7, 2, 4, 2, 3, 7, 4, 5 ]
print(countNumber(num, 4))      # output: 2