def area(x1, y1, l1, x2, y2, l2):
    between_x, between_y = abs(x1 - x2), abs(y1 - y2)

    if between_x >= abs(l1 + l2) / 2 or between_y >= abs(l1 + l2) / 2:
        return 0

    if between_x <= abs(l1 - l2) / 2:
        x = l2
    else:
        x = abs(l1 + l2) / 2 - between_x

    if between_y <= abs(l1 - l2) / 2:
        y = l2
    else:
        y = abs(l1 + l2) / 2 - between_y

    return int(x * y)


print(area(1, 1, 4, 4, 3, 4))  # 2
print(area(1, 1, 4, 3, 6, 4))  # 0
print(area(1, 1, 4, 2, 3, 2))  # 2
print(area(1, 1, 4, 2, 2, 2))  # 4
print(area(1, 1, 4, 2, 1, 2))  # 4
print(area(1, 1, 4, 4, 3, 2))  # 0
