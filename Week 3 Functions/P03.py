import math


def f(x):
    # ADD ADDITIONAL CODE HERE!
    return math.exp(-x) + math.sin(math.pi * (1 + x ** 2) ** 0.5)


def g(x, y):
    # ADD ADDITIONAL CODE HERE!
    return (1 + f(y ** (1 / x))) ** f(y ** (1 / x))


print(f(2), f(3))  # 0.8108255774981366 -0.43822461448665007
print(g(2, 3), g(3, 5))  # 1.0292401354314726 1.0139040096665
