def countSecondQuadrant(p):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    for i in range(len(p)):
        if p[i][0] < 0 and p[i][1] > 0:
            counter += 1
    return counter


points = [[2,1],[-7,4],[-2,-4],[-4,-2],[-2,-1],
          [7,5],[-5,2],[-6,-4],[-3,5],[4,-4],[6,-2]]
print(countSecondQuadrant(points))  # 3