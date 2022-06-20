def accumulate(a):
    n = len(a)
    b = [None] * n

    b[0] = a[0]

    # ADD ADDITIONAL CODE HERE!
    for i in range(1,n):   # note that i start from 1 (not from 0)
        b[i] = b[i-1]+a[i]  

    return b


print(accumulate([2,2,2,2,2]))        # [2,4,6,8,10]
print(accumulate([1,2,3,4,5]))        # [1,3,6,10,15]
print(accumulate([7,6,3,1,5,8,2,4]))  # [7,13,16,17,22,30,32,36]