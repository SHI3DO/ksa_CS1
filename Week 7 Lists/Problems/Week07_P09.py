def area(p):
    n = len(p)
    
    sum = 0
    # ADD ADDITIONAL CODE HERE!
    for i in range(n):
        sum += p[i][0]*(p[(i+1)%n][1] - p[(i-1)%n][1])

    return abs(sum)/2.0

    
points = [[3,1],[6,3],[4,4],[7,6],[2,7],[0,5],[2,3],[1,2]]
print(area(points))    # 22.0
