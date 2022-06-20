def withinRegion(a,c):
    d = int((c/a)**0.5)
    counter = 0
    for x in range(-d,d+1):
        for y in range(-c,c+1):
            if a*x*x-c <= y <= -a*x*x+c:
                counter += 1
    return counter
    
print(withinRegion(1,1))  # 5
print(withinRegion(1,2))  # 11
print(withinRegion(3,5))  # 21
