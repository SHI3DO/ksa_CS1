def smaller(n1, n2):
    # ADD ADDITIONAL CODE HERE!
    if n1 < n2:
        return "left"
    elif n1 > n2:
        return "right"
    else:
        return "equal"


print(smaller(5, 7))  # left
print(smaller(7, 5))  # right
print(smaller(5, 5))  # equal
