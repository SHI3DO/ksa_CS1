def fibonacci(n):
    b = [None] * n

    b[0] = 1
    b[1] = 1

    # ADD ADDITIONAL CODE HERE!
    for i in range(2,n):   # note that i start from 2
        b[i] = b[i-1]+b[i-2]  

    return b


print(fibonacci(5))   # [1,1,2,3,5]
print(fibonacci(10))  # [1,1,2,3,5,8,13,21,34,55]
