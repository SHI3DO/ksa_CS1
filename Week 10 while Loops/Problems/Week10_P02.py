def countEvenDigits(n):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    
    while n > 0:
        if n % 2 == 0:
            counter += 1
        n //= 10

    return counter


print(countEvenDigits(2723))        # 2
print(countEvenDigits(1326924870))  # 6

