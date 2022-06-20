def countWithinCircle(p, r):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    for i in range(len(p)):
        if (p[i][0]**2 + p[i][1]**2) <= r**2:
            counter += 1
    return counter


points = [[2,1],[7,5],[-5,2],[-3,5],[-7,4],[-2,-1],
          [-2,-4],[-4,-2],[-6,-4],[4,-4],[6,-2]]
print(countWithinCircle(points, 3))  # 2
print(countWithinCircle(points, 5))  # 4
print(countWithinCircle(points, 8))  # 9
