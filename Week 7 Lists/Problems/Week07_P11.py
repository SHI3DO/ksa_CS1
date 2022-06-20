def findMin(a):
    min = a[0]

    # ADD ADDITIONAL CODE HERE!
    for i in range(1,len(a)):
        if a[i] < min:
            min = a[i]
    return min


print(findMin([7,8,3,4,3,6]))        # 3
print(findMin([3,5,7,2,7,2,3,8,6]))  # 2