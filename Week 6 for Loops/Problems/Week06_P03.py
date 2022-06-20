def factorial(n):
    prod = 1
    # ADD ADDITIONAL CODE HERE!
    for i in range(2, n+1):
        prod *= i
    return prod


print(factorial(8))   # 40320
print(factorial(12))  # 479001600