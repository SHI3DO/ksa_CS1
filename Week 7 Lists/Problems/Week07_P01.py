def sumSquares(a):
    n = len(a)
    sum = 0
    # ADD ADDITIONAL CODE HERE!
    for i in range(n):
        sum += a[i]**2
    return sum


print(sumSquares([3,5,4]))              # 50
print(sumSquares([2,5,4,0,1,-1,5,1]))   # 73
