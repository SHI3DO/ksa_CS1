def gcd(a,b):
    if a < b:  # swap so that a >= b
        a,b = b,a

    # ADD ADDITIONAL CODE HERE!

    # Euclidean algorithm
    while b != 0:
        # gcd(a, b) = gcd(b, a%b)
        a, b = b, a%b

    return a


print(gcd(36, 20))            # 4
print(gcd(2408208, 2790876))  # 132