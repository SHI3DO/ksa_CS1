def allEven(L):
    for i in range(len(L)):
        if L[i] % 2 == 1:
            return False
    return True
        
def maxOdd(L):
    if allEven(L):
        return 0

    max = 0
    for i in range(len(L)):
        if L[i]%2 == 1 and L[i] > max:
            max = L[i]
    assert max > 0
    return max

print(maxOdd([84,76,42,26,52,40,78,30,48,58]))  # 0
print(maxOdd([14,84,76,26,50,45,65,79,10,3]))   # 79