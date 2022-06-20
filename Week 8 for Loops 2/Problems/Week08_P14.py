def isPrime(p):
    if p <= 1: return False
    for i in range(2, p//2+1):
        if p%i == 0:
            return False
    return True

def countDoublePrime(L):
    counter = 0
    for i in range(len(L)):
        p = L[i]
        if p%2 == 0 and isPrime(p//2):
            counter += 1
    return counter


print(countDoublePrime([6,11,13]))  # 1
print(countDoublePrime([454,878,136,99,702,843,974,203,142,387]))  # 4
print(countDoublePrime([866,8,898,555,158,746,674,886,122,579]))   # 7