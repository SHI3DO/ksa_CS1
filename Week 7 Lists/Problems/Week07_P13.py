def areaTriangle(p1, p2, p3):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    return 0.5*abs((x2*y1+x3*y2+x1*y3)-(x1*y2+x2*y3+x3*y1))

def smallestTriangle(L):
    n = len(L)
    min_area = 10000000
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                area = areaTriangle(L[i],L[j],L[k])
                if area > 0 and area < min_area:
                    min_area = area
    return min_area

print(smallestTriangle([[-9,1],[-8,-5],[4,8],[-2,5],[-9,-7],[-9,2]]))   # 0.5
print(smallestTriangle([[0,-2],[2,-2],[7,-5],[-7,-9],[-7,4],[-5,-2]]))  # 1.5
print(smallestTriangle([[-5,-2],[-9,-7],[-4,-2],[4,6],[1,5],[8,2]]))    # 1.0
print(smallestTriangle([[-4,-3],[-5,8],[-8,3],[-8,6],[6,7],[7,8]]))     # 4.5
print(smallestTriangle([[1,8],[-10,7],[5,6],[-1,-5],[5,6],[4,-5]]))     # 13.0
