import math

def volume(r, side):
    h = (side*side - r*r)**0.5
    v = math.pi * r**2 * h / 3
    return v
    
def largestCone(L):
    max_value = 0
    for i in range(len(L)):
        r = L[i][0]
        side = L[i][1]
        v = volume(r, side)
        if v > max_value:
            max_value = v
    return max_value

print(largestCone([[5,16],[12,19],[4,19],[12,14],[6,8]]))  # 2221.370381814758