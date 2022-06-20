import math

def estimatePI(n):
    sum = 0
    sign = 1
    denom = 1
    while abs(math.pi - sum) >= 10**n:
        sum += 4 * sign * (1/denom)
        sign *= -1
        denom += 2
    return sum
 
print(estimatePI(0))  
print(estimatePI(-1)) 
print(estimatePI(-2)) 
print(estimatePI(-3)) 
print(estimatePI(-4)) 
print(estimatePI(-5)) 
