def isSumOfTwoSquares(num):
    b = int(num**0.5)
    for i in range(b+1):
        for j in range(b+1):
            if num == i**2 + j**2:
                return True
    return False
        
def biggestSumOfTwoSquares(num):
    for n in range(num, 0, -1):
        if isSumOfTwoSquares(n):
            return n
    # cannot reach here
            
print(biggestSumOfTwoSquares(5))  # 5
print(biggestSumOfTwoSquares(6))  # 5
print(biggestSumOfTwoSquares(1))  # 1
print(biggestSumOfTwoSquares(16)) # 16
print(biggestSumOfTwoSquares(19)) # 18
print(biggestSumOfTwoSquares(48)) # 45