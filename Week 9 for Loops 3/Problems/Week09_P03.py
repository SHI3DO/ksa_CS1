def isPrime(p):
    for i in range(2,p//2+1):
        if p%i == 0:
            return False
    return True

def sumOfTwoPrimes(n):
    # ADD ADDITIONAL CODE HERE!
    for i in range(2, n-1):
        for j in range(2, n-1):
            if isPrime(i) and isPrime(j) and n==i+j:
                return True

    return False


for n in range(20, 31):
    print(n, sumOfTwoPrimes(n))