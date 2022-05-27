# ADD FUNCTION HERE!
def ceiling(a):
    f = a - int(a)
    if f > 0:
        return int(a) + 1
    else:
        return int(a)


print(ceiling(2.0))  # output: 2
print(ceiling(2.0000000000001))  # output: 3
print(ceiling(2.99))  # output: 3
