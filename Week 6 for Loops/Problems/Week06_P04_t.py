# copy factorial() in Week06_03.py here, and make use of it

def exp(x):
    sum = 1
    product = 1
    fact = 1
    # ADD ADDITIONAL CODE HERE!
    for i in range(1,100+1):
        product *= x
        fact *= i
        sum += product/fact
    return sum


print(exp(1.0))  # 2.7182818284590455
print(exp(2.0))  # 7.389056098930649
print(exp(4.0))  # 54.598150033144265
