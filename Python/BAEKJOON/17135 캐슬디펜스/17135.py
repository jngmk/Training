N, M, D = map(int, input().split())
archer_list = []
array = [[0] * M]
for _ in range(N):
    n = N - 1
    array[1:0] = [list(map(int, input().split()))]
    n -= 1


def archer(k, now, temp):
    global archer_list
    if k == 3:
        archer_list.append(temp)
    else:
        for a in range(now+1, M):
            archer(k+1, a, temp+[a])


def enemy(nn, arc, a, b):
    global d1, d2, d3
    d1 = a - nn + abs(b - arc[0])
    d2 = a - nn + abs(b - arc[1])
    d3 = a - nn + abs(b - arc[2])


archer(0, -1, [])
max_cnt = 0
for archers in archer_list:
    now = 0
    cnt = 0
    revive = []
    for _ in range(N):
        min1 = min2 = min3 = 999
        d1 = d2 = d3 = 0
        e1 = e2 = e3 = (0, 0)
        n = N
        for x in range(1+now, n+1):
            for y in range(M):
                if array[x][y] == 1:
                    enemy(now, archers, x, y)
                    if min1 >= d1 and D >= d1:
                        if min1 == d1 and e1[1] > y:
                            e1 = (x, y)
                        if min1 > d1:
                            min1 = d1
                            e1 = (x, y)
                    if min2 >= d2 and D >= d2:
                        if min2 == d2 and e2[1] > y:
                            e2 = (x, y)
                        if min2 > d2:
                            min2 = d2
                            e2 = (x, y)
                    if min3 >= d3 and D >= d3:
                        if min3 == d3 and e3[1] > y:
                            e3 = (x, y)
                        if min3 > d3:
                            min3 = d3
                            e3 = (x, y)
        dead = {e1, e2, e3}
        for a, b in dead:
            if a != 0:
                array[a][b] = 0
                cnt += 1
                revive.append((a, b))
        now += 1
        print(array)
    for a, b in revive:
        array[a][b] = 1
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)
