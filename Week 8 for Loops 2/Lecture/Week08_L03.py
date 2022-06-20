def isPrime(p):
    for i in range(2, p//2+1):
        if p % i == 0:
            return False
            
    return True

    
def countPrime(numbers):
    counter = 0
    for i in range(len(numbers)):
        if isPrime(numbers[i]):
            counter += 1
            
    return counter


    
num = [ 217, 287, 181, 143, 163, 319, 233, 399, 203 ]
print(countPrime(num))       # output: 3