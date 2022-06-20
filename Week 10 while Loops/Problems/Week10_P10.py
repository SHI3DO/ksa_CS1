def countWeek(weight, rateA, rateB, x):
    week = 0
    A = (1+x/100)
    B = 1
    while True:
        week += 1
        A *= (1+rateA/100)
        B *= (1+rateB/100)
        if A <= B:
            return week

print(countWeek(200,4,6,10))  # 6
