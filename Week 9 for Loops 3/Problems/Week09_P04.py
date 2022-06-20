def isPrime(p):
    for i in range(2,p//2+1):
        if p%i == 0:
            return False
    return True

def sumOfTwoPrimeSquares(n):
    # ADD ADDITIONAL CODE HERE!
    b = int(n**0.5)
    for i in range(2, b+1):
        for j in range(2, b+1):
            if isPrime(i) and isPrime(j) and n==i**2+j**2:
                return True

    return False

for n in range(50, 61):
    print(n, sumOfTwoPrimeSquares(n))