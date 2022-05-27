def force(m1, m2, r):
    G = 6.67 * 10 ** (-11)

    # ADD ADDITIONAL CODE HERE!
    return G * (m1 * m2 / r ** 2)


print(force(1.5, 1.6, 100.5))  # 1.5849112645726593e-14
