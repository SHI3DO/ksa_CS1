def geometricMean(a):
    n = len(a)
    prod = 1
    # ADD ADDITIONAL CODE HERE!
    for i in range(n):
        prod *= a[i]
    return prod**(1/n)


print(geometricMean([3,2,6,4,7]))         # 3.987421134470927
print(geometricMean([2,4,3,10,7,2,5,6]))  # 4.221167313317658