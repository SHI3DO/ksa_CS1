def isPrime (p):
    for i in range(2,p//2+1):
        if p%i == 0:
            return False
    return True

def countComposite(numbers):
    # ADD ADDITIONAL CODE HERE!
    counter = 0
    for i in range(len(numbers)):
        if not isPrime(numbers[i]):
            counter += 1
    return counter

    
num = [217, 287, 181, 143, 163, 319, 233, 399, 203]
print(countComposite(num))   # 6