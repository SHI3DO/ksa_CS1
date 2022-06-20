def f(i):
    return (i**5 + 2*i**3 + 7*i**2 + i + 500) % 1000


def findMax():
    max = f(0)
    for i in range(100):
        if f(i) > max:
            max = f(i)
    return max


def findMin():
    min = f(0)
    for i in range(100):
        if f(i) < min:
            min = f(i)
    return min

    
def findMinPoint():
    x = 0
    for i in range(100):
        if f(i) < f(x):
            x = i
    return x

    

print("max value:", findMax())
print("min value:", findMin())
print("min point:", findMinPoint())
