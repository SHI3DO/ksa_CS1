def f(a,b,c,x):
    return a*x**2 + b*x + c
    
def minf(a,b,c):
    x0 = -b//(2*a)
    y0 = f(a,b,c,x0)
    y1 = f(a,b,c,x0+1)
    
    if y0 <= y1:
        return y0
    return y1

def S(a,b,k):
    sum = 0
    for i in range(a, b+1):
        sum += i**k
    return sum
    
def minCost(n):
    a = S(0,n-1,2)
    b = -2*S(0,n-1,3)
    c = S(0,n-1,4)
    return minf(a,b,c)

print(minCost(5))   # 24
print(minCost(10))  # 948
print(minCost(15))  # 7952
