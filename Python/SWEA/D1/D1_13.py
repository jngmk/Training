# 2056. 연월일 달력
#

def check_m(month):
    result = False
    if (0 < month < 13):
        result = True
    return result
 
 
def check_d(month, day):
    result = False
     
    if month == 2:
        if 0 < day < 29:
            result = True
    elif month % 2 == 1:
        if (month < 8 and 0 < day < 32):
            result = True
        elif (month > 8 and 0 < day < 31):
            result = True
    else:
        if (month < 8 and 0 < day < 31):
            result = True
        elif (month > 8 and 0 < day < 32):
            result = True
 
    return result
 
 

T = int(input())
for i in range(T):
    date = input()
    month = int(date[4:6])
    day = int(date[6:])
    if (check_m(month) and check_d(month, day)):
        print('#{0} {1}/{2}/{3}'.format(i + 1, date[:4], date[4:6], date[6:]))
    else:
        print('#{0} -1'.format(i + 1))
