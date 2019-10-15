def priority(k, now, tmp):
    global p_list
    # print(k, tmp)
    if now > N+1:
        return
    if k == N//2 + 1:
        # print(tmp)
        p_list.append(tmp)
    else:
        for i in range(now, N, 2):
            priority(k+1, i+2, tmp+[0])
            priority(k+2, i+4, tmp+[1, 1])


def operate():
    global pos
    tmp = []
    while True:
        if pos == N:
            break
        if pos % 2 == 0 and pp[pos//2]:
            pp[pos // 2] = 0
            tmp.append(p_operate())
        else:
            tmp.append(arr[pos])
        if len(tmp) == 3:
            tmp = [calc(int(tmp[0]), tmp[1], int(tmp[2]))]
        pos += 1
        print(tmp, pos)
    return tmp[0]


def p_operate():
    global pos
    tmp1 = []

    while True:
        tmp1.append(arr[pos])
        if len(tmp1) == 3:
            return calc(int(tmp1[0]), tmp1[1], int(tmp1[2]))
        pos += 1
        print('*', tmp1, pos)


def calc(a, b, c):
    if b == '*':
        return a * c
    elif b == '+':
        return a + c
    elif b == '-':
        return a - c


N = int(input())
arr = list(input())
if len(arr) == 1:
    print(arr[0])
else:
    visited = [0] * N
    p_list = []
    priority(0, 0, [])
    result = -9999999999999
    for pp in p_list:
        pos = 0
        print(pp, '-------------')
        result = max(result, operate())
    # print(p_list)
    print(result)
