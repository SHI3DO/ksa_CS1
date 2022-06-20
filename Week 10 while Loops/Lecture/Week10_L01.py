def countDigits(n):
    counter = 0
    
    while n > 0:
        counter += 1
        n //= 10

    return counter

 
print(countDigits(123))
print(countDigits(1357924680))

