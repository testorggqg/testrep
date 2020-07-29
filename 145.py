
def is_nechet(n):
    for i in str(n):
        if int(i)%2 == 0:
            return False
    return True


i = 0
counter = 0
while i < 1000000000:

    i += 1
    if i%10 != 0:
    	h = i + int(str(i)[::-1])
    	if is_nechet(h):
            counter += 1
print(i, counter, sep="  :  ")

