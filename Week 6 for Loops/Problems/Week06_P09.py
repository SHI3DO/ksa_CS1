def isPrime(p):
    if p <= 1: return False
    for i in range(2, p//2+1):
        if p%i == 0: 
            return False
    return True

def maxPrimeFactor(n):
    for p in range(n,1,-1):
        if isPrime(p) and n%p==0:
            return p

print(maxPrimeFactor(100))  # 5
print(maxPrimeFactor(97))   # 97
print(maxPrimeFactor(85))   # 17
print(maxPrimeFactor(99))   # 11
