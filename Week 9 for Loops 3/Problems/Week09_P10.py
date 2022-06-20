def tripleSum(data, goal):
    for i in range(len(data)):
        for j in range(i+1, len(data)) :
            for k in range(j+1, len(data)):
                if data[i]+data[j]+data[k] == goal:
                    return True
    return False
                

print(tripleSum([5,12,3,8,12,11,2,6], 16))         # True
print(tripleSum([5,12,3,8,12,11,2,6], 26))         # True
print(tripleSum([5,12,3], 9))                      # False  
print(tripleSum([1,2,3,4,1,2,2,1,1,1], 16))        # False 
print(tripleSum([5,0,1,-1,-4,-2,2,3,1,6,4,-5], -14))  # False 
print(tripleSum([5,1,2,-3,8,0,2,-11,2,6], 20))     # False 
print(tripleSum([3,6,3], 12))                      # True
print(tripleSum([-4,0,1,-1,-4,-2,2,3,1,6,4,-5], -12)) # False 
print(tripleSum([5,1,2,-3,8,12,-11,2,6], 19))      # True 
print(tripleSum([0,1,-1,-2,4], 0))                 # True
