def reverse(a):
    n = len(a)
    b = [None] * n

    for i in range(n):
        #b[i] = a[n-1-i]  # ADD ADDITIONAL CODE HERE!
        b[i] = a[-1-i]

    return b


print(reverse([3,1,5,2,4]))        # [4,2,5,1,3]
print(reverse([7,6,3,1,5,8,2,4]))  # [4,2,8,5,1,3,6,7]