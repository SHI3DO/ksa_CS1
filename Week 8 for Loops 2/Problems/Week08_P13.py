def average(M):
    n = len(M)
    sum = 0
    for i in range(n):
        sum += M[i]
    return sum/n

def standardDeviation(M):
    ave = average(M)
    n = len(M)
    sum = 0
    for i in range(n):
        sum += (M[i]-ave)**2
    return (sum/n)**0.5

def countWithinRange(L):
    n = len(L)
    M = [None]*n
    for i in range(n):
        M[i] = L[i]**3

    ave = average(M)
    sigma = standardDeviation(M)

    counter = 0
    for i in range(n):
        if abs(M[i]-ave) <= sigma: #ave-sigma <= M[i] <= ave+sigma:
            counter += 1
    return counter
        
print(countWithinRange([2,3,4,7,8,9,13,14,15]))  # 7  