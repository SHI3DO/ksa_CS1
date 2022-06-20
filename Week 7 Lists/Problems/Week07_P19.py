def inversePermutation(a):
    b = [None] * len(a)
    for i in range(len(a)):
        b[a[i]] = i
    return b

print(inversePermutation([6,5,4,9,8,7,3,2,1,0]))  # [9,8,7,6,2,1,0,5,4,3]