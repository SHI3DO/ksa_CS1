def withinRect(top, bottom, left, right, x, y):
    # ADD ADDITIONAL CODE HERE!
    return (left <= x <= right and bottom <= y <= top)


print(withinRect(2,-4,-5,6, -5,2))  # True
print(withinRect(2,-4,-5,6, 6,-1))  # True
print(withinRect(2,-4,-5,6, 0,1))   # True
print(withinRect(2,-4,-5,6, -6,0))  # False
print(withinRect(2,-4,-5,6, 0,3))   # False
print(withinRect(2,-4,-5,6, 6,3))   # False



print("==============================================")

def countWithinRect(top, bottom, left, right, p):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    for i in range(len(p)):
        if withinRect(top, bottom, left, right, p[i][0], p[i][1]):
            counter += 1
    return counter


points = [[2,1],[7,5],[-5,2],[-3,5],[-7,4],[-2,-1],
          [-2,-4],[-4,-2],[-6,-4],[4,-4],[6,-2]]
print(countWithinRect(2,-4,-5,6, points))  # 7