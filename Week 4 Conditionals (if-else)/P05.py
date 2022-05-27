def round(x):
    fraction = x - int(x)

    if fraction >= 0.5:
        return int(x) + 1
    else:
        return int(x)
    # ADD ADDITIONAL CODE HERE!


print(round(2.4))  # 2
print(round(2.5))  # 3
print(round(2.6))  # 3
