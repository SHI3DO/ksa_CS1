import math

def factorial(n):  # Week06_P03.py
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

def estimatePI():
    sum = 0.0
    k = 0
    factor = 2 * 2**0.5 / 9801
    """
    while True:
        num = factorial(4*k) * (1103.0 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        sum += factor * num / den
        if abs(math.pi - 1/sum) < 10**(-15): 
            return 1/sum
        k += 1
    """
    #num = 1103.0
    #den = 1.0
    #sum += factor * num / den
    estPi = 0
    while abs(math.pi - estPi) >= 10**(-15):
        #k += 1  
        num = factorial(4*k) * (1103.0 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        sum += factor * num / den
        estPi = 1/sum
        k += 1
    return 1/sum
    
    
print(estimatePI())