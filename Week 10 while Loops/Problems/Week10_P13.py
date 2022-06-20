def toDecimal(n):
    a = n[0]     # number
    b = n[1]     # number system  

    if a >= 0:
        sign = 1
    else:
        sign = -1
    a = a*sign

    sum = 0
    k = 0
    while a>0:
        digit = a%10
        sum += digit*(b**k)
        k += 1
        a = a//10
    return sum*sign

def findMax(L) :
    max = toDecimal(L[0])
    for i in range(1,len(L)):
        num = toDecimal(L[i])
        if num > max:
            max = num
    return max

print(findMax([[151,8],[1111001,2],[-10101,2],[2731,8],[1001,10]]))  # 1497
