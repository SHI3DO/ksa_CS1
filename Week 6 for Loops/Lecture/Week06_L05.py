def power(x, n):
    product = 1
    for i in range(n): # i: 0,1,...n-1
        product *= x
    return product


def power2(x,n):
    product = 1
    for i in range(1, n+1): # i: 1,2,...n
        product *= x
    return product


print(power(2,10))
print(power2(2,10))
        