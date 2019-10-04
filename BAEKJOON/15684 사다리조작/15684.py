def construct(k, ni, nj):
    global flag
    if k == n and manipulate():
        flag = True
    if flag:
        return
    else:
        if nj == H + 1:
            ni += 1
            nj = 0
        for i in range(ni, N):
            for j in range(nj, H+1):
                if ladders[j][i] != 0:
                    continue
                ladders[j][i] = -1
                ladders[j][i+1] = -2
                construct(k+1, ni, nj+1)
                ladders[j][i] = 0
                ladders[j][i+1] = 0


def manipulate():
    for line in range(1, N+1):
        s = line
        for l in range(1, H+1):
            if ladders[l][s] == -1:
                s += 1
            elif ladders[l][s] == -2:
                s -= 1
        if s != line:
            return False
    return True


N, M, H = map(int, input().split())
ladders = [[0] * (N+1) for _ in range(H+1)]
flag = False
result = -1
for _ in range(M):
    a, b = map(int, input().split())
    ladders[0][b] += 1
    ladders[a][b] = -1
    ladders[a][b+1] = -2

print(ladders)

for n in range(4):
    construct(0, 0, 0)
    if flag:
        result = n
        break

print(result)
