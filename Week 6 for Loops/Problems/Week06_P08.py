def combination(n,k):
    prod = 1
    for i in range(1,k+1):
        prod *= n+1-i
    for i in range(1,k+1):
        prod //= i
    return prod
   
print(combination(7,3))    # 35
print(combination(250,2))  # 31125