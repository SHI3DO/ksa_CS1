def countDigits(n):  # Week10_L01.py
    counter = 0
    while n > 0:
        counter += 1
        n //= 10
    return counter

def evenDigits(num):
    l = countDigits(num)
    r = 0
    for i in range(l):
        digit = (num // 10**(l-i-1)) % 10
        if digit%2 == 0:
            r = r*10 + digit
    return r
        
print(evenDigits(277890)+1)     # 281 
print(evenDigits(2778908421)+1) # 280843
print(evenDigits(24312)+1)      # 243