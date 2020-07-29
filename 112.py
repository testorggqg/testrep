


def is_increasing(n):
    h=0
    for i in str(n):
        if int(i) >= h:
            h = int(i)
        else:
            return False
    return True


def is_decreasing(n):
    h=9
    for i in str(n):
        if int(i) <= h:
            h = int(i)
        else:
            return False
    return True

s = 0
bouncers = 0
part = 0
while part < 0.99:
#while s < 1001:
    s+=1
    if is_decreasing(s) == False and is_increasing(s) == False:
       	bouncers += 1
    part = bouncers/float(s)
    print(s, bouncers, part, sep = "  :  ")

