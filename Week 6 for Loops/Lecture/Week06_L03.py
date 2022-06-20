for k in range(1, 11):
    if k % 2 == 0:
        print(k, "is even")
    else:
        print(k, "is odd")


print() ; print()
        
for i in range(1, 10):
    for j in range(1, i+1):
        print(i*j, end="")
        for k in range(3):
            print(end=" ")
    print()