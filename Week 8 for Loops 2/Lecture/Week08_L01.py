def countOdd(numbers):
    counter = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            counter += 1
            
    return counter

    
num = [ 1, 7, 2, 4, 2, 3, 7, 4, 5 ]
print(countOdd(num))       # output: 5