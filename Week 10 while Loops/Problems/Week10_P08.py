import math

def estimatePI(n):
    sum = 0
    pi = 0
    i = 1
    while abs(math.pi - pi) >= 10**n:
        sum += 1/i**2
        pi = (6*sum)**0.5
        i += 1
    return pi
    
print(estimatePI(-3)) 
print(estimatePI(-4)) 
print(estimatePI(-5)) 
 