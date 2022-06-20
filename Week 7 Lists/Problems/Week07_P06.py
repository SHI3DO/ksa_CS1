def square(a):
    # ADD ADDITIONAL CODE HERE!
    n = len(a)
    b = [None] * n

    for i in range(n):
        b[i] = a[i]**2  

    return b

L = [7,6,3,1,5,8,2,4]
print(square(L))  # [49,36,9,1,25,64,4,16]
print(L)          # [7,6,3,1,5,8,2,4]