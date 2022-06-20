def countSevens(n):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    
    while n > 0:
        if n % 10 == 7:
            counter += 1
        n //= 10

    return counter


print(countSevens(1723))        # 1
print(countSevens(1357924770))  # 3