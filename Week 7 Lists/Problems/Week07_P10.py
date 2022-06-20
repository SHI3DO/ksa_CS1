# ADD FUNCTION HERE!
def perimeter(p):
    n = len(p)
    
    sum = 0
    for i in range(n):
        j = (i+1)%n
        sum += ((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)**0.5

    return sum

    
points = [[3,1],[6,3],[4,4],[7,6],[2,7],[0,5],[2,3],[1,2]]
print(perimeter(points))    # 23.85332583138582
