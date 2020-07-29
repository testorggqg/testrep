from math import sqrt


def check_form(n):
    number = str(n)
    form = "1_2_3_4_5_6_7_8_9_0"
    for k in range(0,len(form),2):
        if number[k] != form[k]:
            return False
    return True


start = int(sqrt(10**18))
end = int(sqrt(20**18))
print("Start: {}".format(str(start)))
print("End: {}".format(str(end)))
for i in range(start,end):
    if check_form(i**2):
        print(i, i**2, sep="  :  ")
