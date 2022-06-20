def func(b):
    a = [None] * len(b)
    for i in range(len(a)):
        a[i] = b[i] + 1
    return a

    
num = [ 2, 4, 3, 1, 7, 2, 5, 6 ]
c = func(num)
print(c)