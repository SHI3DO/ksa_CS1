def sumInterval(L, i, j):
    sum = 0
    for k in range(i,j+1):
        sum += L[k]
    return sum
        
def maxInterval(L): # O(N^3)
    n = len(L)
    max_sum = 0
    for i in range(n):
        for j in range(i,n):
            sum_ij = sumInterval(L, i, j)
            if sum_ij > max_sum:
                max_sum = sum_ij
    return max_sum

def maxInterval(L): # O(N)
    max_sum = this_sum = 0
    for j in range(len(L)):
        this_sum += L[j]
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum

print(maxInterval([-8, 7, 6, -5, 0, -1, 3, 6, -9, -10, 7, -1, 6, \
                   -10, -1, 5, -6, 9, 8, -10, -10, 1, 9, -2, -6, \
                   -2, -10, -6, -1, 0])) # 17
print(maxInterval([-6, -8, 5, -7, -9, -2, 9, 6, 6, -6, 1, -5, -7, \
                   -8, -6, 9, 7, 6, 6, -6, -4, 3, 5, 7, 8, -9, 2, \
                   4, 0, -7]))  # 41
print(maxInterval([-1, -3, -8, 8, -10, 0, 3, -9, 1, 2, -10, -3, 4, \
                   -1, 5, -7, -6, -8, 0, 9, 2, 6, -2, 5, -8, -4, 4, \
                   5, -2, -9]))   # 20
