def blood(supplyO, supplyA, supplyB, supplyAB,
          demandO, demandA, demandB, demandAB):
    if supplyO < demandO:
        return False
    if supplyA + supplyO < demandA + demandO:
        return False
    if supplyB + supplyO < demandB + demandO:
        return False
    if supplyAB + supplyO + supplyA + supplyB < demandAB + demandO + demandA + demandB:
        return False
    return True
    # ADD ADDITIONAL CODE HERE!


print(blood(50, 36, 11, 8, 45, 42, 10, 3))  # False
print(blood(50, 36, 11, 3, 45, 38, 10, 7))  # True
