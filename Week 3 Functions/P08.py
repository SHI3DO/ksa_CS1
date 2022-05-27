def countCoins(cent):
    count = 0
    coinarray = [100, 25, 10, 5, 1]
    for coin in coinarray:
        count += cent // coin
        cent %= coin

    return count


print(countCoins(34))  # 6
print(countCoins(242))  # 7
