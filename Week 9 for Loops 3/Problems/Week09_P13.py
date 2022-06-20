def isPrime(p):
    if p <= 1: return False
    for i in range(2, p//2+1):
        if p%i == 0:
            return False
    return True

def check(n):
    for i in range(2, n-1):
        for j in range(i+1, n-1):
            if isPrime(i) and isPrime(j) and n==i+j:
                return True
    return False

def sumOfTwoDistinctPrimes(L):
    counter = 0
    for i in range(len(L)):
        if check(L[i]):
            counter += 1
    return counter


print(sumOfTwoDistinctPrimes([4,6,10]))  # 1
print(sumOfTwoDistinctPrimes([254,79,137,12,251,229,135,71,270,11]))   # 4
print(sumOfTwoDistinctPrimes([114,260,152,27,186,116,137,50,36,277]))  # 7
