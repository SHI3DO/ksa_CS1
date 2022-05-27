def leapYear(year):
    if year % 4 != 0:
        return False
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return True

    # now, year is divisible by 4
    # ADD ADDITIONAL CODE HERE!


print(leapYear(2008), leapYear(2011), leapYear(2012))  # True False True
print(leapYear(2000), leapYear(2100), leapYear(2200))  # True False False
print(leapYear(2300), leapYear(2400), leapYear(3200))  # False True True

print("==============================================")


def numDays(year, month):
    assert (1 <= month <= 12)

    if month == 1 or month == 3 or month == 5 or month == 7 or \
            month == 8 or month == 10 or month == 12:
        return 31
    elif month != 2:
        return 30
    else:
        if leapYear(year):
            return 29
        else:
            return 28

    # ADD ADDITIONAL CODE HERE!


print(numDays(2000, 1), numDays(2001, 4), numDays(2004, 8))  # 31 30 31
print(numDays(2004, 9), numDays(2005, 3), numDays(2005, 7))  # 30 31 31
print(numDays(2008, 2), numDays(2011, 2), numDays(2012, 2))  # 29 28 29
print(numDays(2000, 2), numDays(2100, 2), numDays(2200, 2))  # 29 28 28
print(numDays(2300, 2), numDays(2400, 2), numDays(3200, 2))  # 28 29 29
