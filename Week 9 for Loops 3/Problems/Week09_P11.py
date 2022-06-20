def bmi(h,w):
    return w / (h/100)**2

def BMIWithinRange(data, a, b):
    for i in range(len(data)):
        h = data[i][0]
        w = data[i][1]
        if not (a <= bmi(h,w) <= b):
            return False
    return True

    
print(BMIWithinRange([[165,48],[176,69],[186,80],[161,64],[183,97]],15,22)) # False 
print(BMIWithinRange([[163,70],[199,67],[156,59],[186,70],[191,73]],10,29)) # True
print(BMIWithinRange([[165,48]],15,20))                                     # True
print(BMIWithinRange([[199,67],[186,70],[191,73]],22,24))                   # False
print(BMIWithinRange([[175,48],[146,69],[186,83],[161,64],[183,97]],15,26)) # False 
print(BMIWithinRange([[183,70],[199,67],[156,59],[186,73]],10,30))          # True
print(BMIWithinRange([[195,68],[176,69],[156,80],[161,74],[183,97]],19,22)) # False 
print(BMIWithinRange([[143,74],[199,67],[156,59],[186,80],[191,73]],10,28)) # False
print(BMIWithinRange([[161,48],[176,69],[186,80],[161,64],[183,97]],16,30)) # True
print(BMIWithinRange([[166,60],[199,67],[156,59],[186,70],[191,73]],20,30)) # False