# ADD FUNCTION HERE!
def reverse(n):
    return (n % 10) * 1000 + ((n // 10) % 10) * 100 + ((n // 100) % 10) * 10 + n // 1000


print(reverse(3702))  # 2073
print(reverse(3710))  # 173
print(reverse(3700))  # 73
