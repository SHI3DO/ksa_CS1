def func(number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    return sum

        
num = [ 2, 4, 3, 1, 7, 2, 5, 6 ]
s = func(num)
print(s)