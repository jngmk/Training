from collections import deque


def rotate(n):
    global rotate_arr
    tmp1 = []
    for i in range(5):
        tmp = []
        for j in range(5):
            tmp.append(arr[n][i][j])
        tmp1.append(tmp)
    rotate_arr[n][0] = tmp1
    tmp1 = []
    for j in range(4, -1, -1):
        tmp = []
        for i in range(5):
            tmp.append(arr[n][i][j])
        tmp1.append(tmp)
    rotate_arr[n][1] = tmp1
    tmp1 = []
    for j in range(5):
        tmp = []
        for i in range(4, -1, -1):
            tmp.append(arr[n][i][j])
        tmp1.append(tmp)
    rotate_arr[n][2] = tmp1
    tmp1 = []
    for i in range(4, -1, -1):
        tmp = []
        for j in range(4, -1, -1):
            tmp.append(arr[n][i][j])
        tmp1.append(tmp)
    rotate_arr[n][3] = tmp1


def solve(x, y, z, cnt):
    global result, q
    r = {0: e, 1: d, 2: c, 3: b, 4: a}
    if cnt == 12:
        result = 12
        return
    if cnt >= result:
        return
    else:
        for di in range(6):
            vx = x+dx[di]; vy = y+dy[di]; vz = z+dz[di]
            if 0 <= vx < 5 and 0 <= vy < 5 and 0 <= vz < 5:
                if not visited[vx][vy][vz]:
                    if di < 4:
                        if rotate_arr[vz][r[vz]][vx][vy]:
                            visited[vx][vy][vz] = 1
                            solve(vx, vy, vz, cnt+1)

    pass


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
arr = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
rotate_arr = [[0] * 4 for _ in range(5)]
visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
result = 125
q = deque()
for zz in range(5):
    rotate(zz)
del arr

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    if rotate_arr[0][e][0]:
                        solve(0, 0, 0, 0)
