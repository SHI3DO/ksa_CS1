def sumNumbers(n):
    sum = 0
    
    for i in range(1,n+1): # repeat for each i = 1,2,...,n
        sum = sum + i
        
    return sum


print(sumNumbers(10))
print(sumNumbers(100))
print(sumNumbers(10000))