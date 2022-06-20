def countOutOfCircle(L, r):
    counter = 0
    for i in range(len(L)):
        p = L[i]
        if p[0]**2 + p[1]**2 > r**2:
            counter += 1
    return counter
        
print(countOutOfCircle([[-3,2],[3,3],[-8,-7],[2,2],[4,3]], 1)) # 5
print(countOutOfCircle([[-3,2],[3,3],[-8,-7],[2,2],[4,3]], 5)) # 1
print(countOutOfCircle([[8,8],[3,3],[-8,-7],[8,8],[4,3]], 5))  # 3