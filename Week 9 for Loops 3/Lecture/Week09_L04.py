import math

def isPrime(p):
    for i in range(2, p//2+1):
        if p % i == 0:       # not (p % i != 0)
            return False
            
    return True



for i in range(20,30):
    print(i, isPrime(i))