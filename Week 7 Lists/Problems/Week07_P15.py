def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ** 0.5

def centerPosition(L):
    x = 0
    y = 0
    for i in range(len(L)):
        x += L[i][0]
        y += L[i][1]
    return [x/len(L), y/len(L)]
 
def outlier(L):
    center = centerPosition(L)
    p = L[0]
    max_dist = distance(center,p)
    for i in range(1,len(L)):
        dist = distance(center,L[i])
        if dist > max_dist:
            max_dist = dist
            p = L[i]
    return p

print(outlier([[1,2],[9,2],[4,8],[7,4],[1,-2],[-1, 4]]))  # [9,2]