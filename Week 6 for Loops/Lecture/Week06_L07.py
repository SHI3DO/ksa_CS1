def printTriangle(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j >= i:
                print("* " , end="")
            else:
                print(". " , end="")
        print()


def printTriangle2(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j > n-i:
                print("* " , end="")
            else:
                print(". " , end="")
        print()
        

def printDiamond(n):
    for y in range(n, -n-1, -1):
        for x in range(-n, n+1):
            if abs(x) + abs(y) <= n:
                print("* " , end="")
            else:
                print(". " , end="")
        print()


printTriangle(6)
print()
printTriangle2(6)
print()
printDiamond(4)
