def numDays(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if year%4 != 0:
        return 28
    if year%100 != 0:
        return 29
    if year%400 != 0:
        return 28
    return 29

def nextNDay(L):
    year = L[0]
    month = L[1]
    day = L[2]
    N = L[3]
    
    for i in range(N):
        day += 1
        if day > numDays(year, month):
            day = 1
            month += 1
        if month > 12:
            month = 1
            year += 1

    return [year, month, day]
        
print(nextNDay([2014,5,25,1]))      # [2014,5,26]
print(nextNDay([1969,4,19,16500]))  # [2014,6,22]
print(nextNDay([1967,6,13,15000]))  # [2008,7,7]
print(nextNDay([1989,3,2,20000]))   # [2043,12,4]
print(nextNDay([1700,1,25,2000]))   # [1705,7,18]
