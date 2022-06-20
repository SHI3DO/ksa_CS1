n = 10

for k in range(n):
    print(k, end=" ")     # 0 1 ... n-1

print()
    
for k in range(1, n+1):
    print(k, end=" ")     # 1 2 ... n

print()
    
for k in range(10, 21, 2):
    print(k, end=" ")     # 10 12 14 16 18 20

print()
    
for k in range(n, 0, -1):
    print(k, end=" ")     # n n-1 ... 2 1


print()

sum = 0
for k in range(n):
    sum += k
print(sum)