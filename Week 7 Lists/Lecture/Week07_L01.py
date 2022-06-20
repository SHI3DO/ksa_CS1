number = [ 2, 4, 3, 1, 7, 2, 5, 6 ]

sum = 0
sum += number[0] # 2
sum += number[1] # 4
sum += number[2] # 3
sum += number[3] # 1
sum += number[4] # 7
sum += number[5] # 2
sum += number[6] # 5
sum += number[7] # 6
print(sum)



sum = 0
for i in range(len(number)):  # len(number): 8
    sum += number[i]
print(sum)