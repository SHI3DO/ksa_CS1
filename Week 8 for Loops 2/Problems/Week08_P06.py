def leapYear(year):
    if year%4 != 0:
        return False
    if year%100 != 0:
        return True
    return (year%400 == 0)


def countLeapYear(numbers):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    for i in range(len(numbers)):
        if leapYear(numbers[i]):
            counter += 1
    return counter


print(countLeapYear([2008,2011,2012,2000]))  # 3
print(countLeapYear([2100,2300,2400,2200]))  # 1
