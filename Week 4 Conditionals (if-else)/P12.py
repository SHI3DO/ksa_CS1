def triangular(n):
    m = int((2 * n) ** 0.5)
    if m * (m + 1) == 2 * n:
        return m
    else:
        return "None"
    # ADD ADDITIONAL CODE HERE!


print(triangular(11981467576204192310))  # None
print(triangular(62208609168654078198))  # None
print(triangular(37739325663055308061))  # 8687845033
print(triangular(10142437317447395278))  # 4503873292
