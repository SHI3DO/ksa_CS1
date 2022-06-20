def reverse(n):
    sum = 0
    while n>0:
        digit = n%10
        sum += digit
        n = n//10
        sum = sum*10
    return sum//10

def reverseSum(L):
    sum = 0
    for i in range(len(L)):
        sum += reverse(L[i])
    return sum

print(reverseSum([12,40,2]))  # 27  
