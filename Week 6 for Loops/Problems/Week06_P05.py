def withinCircle(r):
    counter = 0

    for x in range(-r,r+1):
        for y in range(-r,r+1):
            # ADD ADDITIONAL CODE HERE!
            if x**2 + y**2 <= r**2:
                counter += 1

    return counter

    
print(withinCircle(100)/100**2)     # 3.1417
print(withinCircle(1000)/1000**2)   # 3.141549