def threshold(dailyGains, goal): 
    sum = 0
    for i in range(len(dailyGains)):
        sum += dailyGains[i]
        if sum >= goal:
            return i+1
    return 0

print(threshold([5,-3,8,2,-9,11,4,5], 17))  # 7  
print(threshold([5,3,8,4,-2,3,2,9,1], 16))  # 3 
print(threshold([15,-3,8,22,9,1], 15))      # 1 
print(threshold([5], 4))                    # 1 
print(threshold([5,3,8,2,9,1,1,23,4], 57))  # 0 
