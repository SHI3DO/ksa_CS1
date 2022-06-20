import math

def sumOfTwoSquares(n):
    b = int(math.sqrt(n))
    
    for i in range(1, b+1):
        for j in range(1, b+1):
            if n == i*i + j*j:
                return True
                
    return False



for i in range(20,30):
    print(i, sumOfTwoSquares(i))