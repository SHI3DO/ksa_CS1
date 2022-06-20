def toBinary(n):
    if n < 0:
        sign = -1
        n = -n
    else:
        sign = 1

    sum = 0
    k = 0
    while n > 0:
        bit = n%2
        sum += bit*(10**k)
        k += 1
        n //= 2
    return sign*sum

def countZeros(n):  # similar to Week10_P01.py
    counter = 0
    while n > 0:
        if n % 10 == 0:
            counter += 1
        n //= 10
    return counter

def countAllZeros(L):
    counter = 0
    for i in range(len(L)):
        counter += countZeros(toBinary(L[i]))
    return counter
    
print(countAllZeros([10,20,30]))  # 6