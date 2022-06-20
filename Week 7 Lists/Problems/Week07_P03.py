def harmonicMean(a):
    n = len(a)
    # ADD ADDITIONAL CODE HERE!
    sum = 0
    for i in range(n):
        sum += 1/a[i]
    return n/sum


print(harmonicMean([3,2,6,4,7]))         # 3.58974358974359
print(harmonicMean([2,4,3,10,7,2,5,6]))  # 3.648208469055375