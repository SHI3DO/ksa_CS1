def f(i,j):
    return (i**5 + 2*(i**3)*(j**2) + 5*i**2 + j + 5000) % 10000


def findMax():
    max = f(0,0)
    
    for i in range(100):
        for j in range(100):
            # ADD ADDITIONAL CODE HERE!
            if f(i,j) > max:
                max = f(i,j)
                
    return max

    
print("max value:", findMax())    # 9997
