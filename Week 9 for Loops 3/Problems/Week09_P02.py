def sumOfThreeDistinctSquares(n):
    # ADD ADDITIONAL CODE HERE!
    b = int(n**0.5)

    for i in range(1, b+1):
        for j in range(i+1, b+1):
            for k in range(j+1, b+1):
                if n == i*i + j*j + k*k:
                    return True

    return False


for n in range(20, 31):
    print(n, sumOfThreeDistinctSquares(n))