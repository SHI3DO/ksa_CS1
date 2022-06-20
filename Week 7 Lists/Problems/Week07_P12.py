def distSquared(p1, p2):
    return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2

def closestPair(p):
    n = len(p)
    min = distSquared(p[0], p[1])
    
    # ADD ADDITIONAL CODE HERE!
    for i in range(n):
        for j in range(i+1,n):
            d = distSquared(p[i], p[j])
            if d < min:
                min = d

    return min**0.5

    
points = [[4,-4],[7,5],[2,1],[-2,-1],[-3,5]]
print(closestPair(points))   # 4.47213595499958
                             # (distance bet'n [2,1] and [-2,-1])