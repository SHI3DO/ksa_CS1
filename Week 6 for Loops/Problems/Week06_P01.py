def printMultTable0():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i*j, end=" ")
        print()

def printMultTable1():
    # ADD ADDITIONAL CODE HERE!
    for i in range(1, 10, 2):
        for j in range(1, 10):
            print(i*j, end=" ")
        print()

def printMultTable2():
    # ADD ADDITIONAL CODE HERE!
    for i in range(1, 10, 2):
        for j in range(1, i+1):
            print(i*j, end=" ")
        print()

        

print("==========================")
printMultTable0()
print("==========================")
printMultTable1()
print("==========================")
printMultTable2()
