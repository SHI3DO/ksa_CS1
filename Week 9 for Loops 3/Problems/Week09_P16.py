def isPeak(L, k):
    for i in range(k,0,-1): #for i in range(k):
        if L[i-1] >= L[i]:
            return False
    for i in range(k,len(L)-1):
        if L[i] <= L[i+1]:
            return False
    return True
def maxIndex(L):
    mIndex = 0
    for i in range(1,len(L)):
        if L[i] > L[mIndex]:
            mIndex = i
    return mIndex

def mountain(L):
    """
    for k in range(1,len(L)-1):
        if isPeak(L,k):
            return L[k]
    return None
    """
    mIndex = maxIndex(L)
    if mIndex==0 or mIndex==len(L):
        return None
    if isPeak(L,mIndex):
        return L[mIndex]
    return None
    
print(mountain([1,1,1]))    # None
print(mountain([1,2,3,3]))  # None
print(mountain([1,2,3,4,5]))  # None
print(mountain([5,4,3,2,1]))  # None
print(mountain([2,1,3,2,4,3,5]))  # None
print(mountain([1,2,3,4,5,6,0]))  # 6
print(mountain([1,2,3,4,5,4,3,2,1]))   # 5 
print(mountain([1,2,3,4,5,5,4,3,2,1])) # None
print(mountain([12,23,25,37,88,76,54,32,1]))  # 88
print(mountain([12,23,25,37,188,76,54,32,1]))  # 188
