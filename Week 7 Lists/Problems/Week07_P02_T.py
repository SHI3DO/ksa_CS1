def computePolynomial (a, x):
    n = len(a)
    sum = 0
    # ADD ADDITIONAL CODE HERE!
    xp= 1
    for i in range(n):
        sum += a[i] * xp
        xp *= x
    return sum


print(computePolynomial([3,5,4], 5))              # 128
print(computePolynomial([2,0,4,0,1,-1,5,1], 3))   # 5708
