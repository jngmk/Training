from itertools import permutations


def rotate(n):
    global rotate_arr
    tmp1 = []
    for i in range(5):
        tmp = []
        for j in range(5):
            tmp.append(arr[n][i][j])
        tmp1.append(tmp)
    rotate_arr[n].append(tmp1)
    tmp1 = []
    for j in range(4, -1, -1):
        tmp = []
        for i in range(5):
            tmp.append(arr[n][i][j])
        tmp1.append(tmp)
    if tmp1 not in rotate_arr[n]:
        rotate_arr[n].append(tmp1)
    tmp1 = []
    for j in range(5):
        tmp = []
        for i in range(4, -1, -1):
            tmp.append(arr[n][i][j])
        tmp1.append(tmp)
    if tmp1 not in rotate_arr[n]:
        rotate_arr[n].append(tmp1)
    tmp1 = []
    for i in range(4, -1, -1):
        tmp = []
        for j in range(4, -1, -1):
            tmp.append(arr[n][i][j])
        tmp1.append(tmp)
    if tmp1 not in rotate_arr[n]:
        rotate_arr[n].append(tmp1)


def solve(x, y, z, cnt):
    global result
    r = {0: e, 1: d, 2: c, 3: b, 4: a}
    if (x, y, z) == (4, 4, 4):
        result = min(result, cnt)
        return
    if cnt >= result:
        return
    else:
        for di in range(6):
            if 0 <= x+dx[di] < 5 and 0 <= y+dy[di] < 5 and 0 <= z+dz[di] < 5:
                vx = x + dx[di]; vy = y + dy[di]; vz = z + dz[di]
                if not visited[vx][vy][vz]:
                    if rotate_arr[order[vz]][r[vz]][vx][vy]:
                        visited[vx][vy][vz] = 1
                        solve(vx, vy, vz, cnt+1)
                        visited[vx][vy][vz] = 0


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
arr = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
rotate_arr = {}
for idx in range(5):
    rotate_arr.update({idx: []})
visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
visited[0][0][0] = 1
result = 125
for zz in range(5):
    rotate(zz)

ordering = list(permutations(list(range(5)), 5))
for order in ordering:
    if result == 12: break
    for a in range(len(rotate_arr[order[4]])):
        if result == 12: break
        for b in range(len(rotate_arr[order[3]])):
            if result == 12: break
            for c in range(len(rotate_arr[order[2]])):
                if result == 12: break
                for d in range(len(rotate_arr[order[1]])):
                    if result == 12: break
                    for e in range(len(rotate_arr[order[0]])):
                        if result == 12: break
                        if rotate_arr[order[0]][e][0][0] and rotate_arr[order[4]][a][4][4]:
                            solve(0, 0, 0, 0)
print(result if result != 125 else -1)
