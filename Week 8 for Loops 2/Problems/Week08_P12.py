def countLower(L): 
    sum = 0.0
    for i in range(len(L)):
        sum += L[i]
    ave = sum / len(L)

    counter = 0
    for i in range(len(L)):
        if L[i] < ave:
            counter += 1
    return counter
    
print(countLower([10,10,10,10,10]))  # 0
print(countLower([1,2,3,4,5,6,7,8,9,10]))  # 5
print(countLower([4,5,83,234,562,13,-976,-75,34]))  # 2
print(countLower([-123,32,4,346,7,-433,8,4,53,298,43]))  # 6
