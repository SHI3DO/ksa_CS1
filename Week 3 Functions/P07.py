# ADD FUNCTION HERE!
def countCoins(n):
    return int(n / 500) + int((n % 500) / 100) + int((n % 100) / 50) + int((n % 50) / 10)


print(countCoins(730))  # 6
print(countCoins(790))  # 8
print(countCoins(260))  # 4
print(countCoins(70))  # 3
