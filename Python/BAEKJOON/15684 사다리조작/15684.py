def construct(k, ni, nj):
    global result
    if result <= k:
        return
    if manipulate():
        result = min(result, k)
    if k == 3:
        return
    else:
        for j in range(nj, H+1):
            if nj != j:
                ni = 1
            for i in range(ni, N):
                if ladders[j][i] or ladders[j][i+1] or ladders[j][i-1]:
                    continue
                ladders[j][i] = 1
                construct(k+1, i+1, j)
                ladders[j][i] = 0


def manipulate():
    for line in range(1, N+1):
        s = line
        for l in range(1, H+1):
            if ladders[l][s]:
                s += 1
            elif ladders[l][s-1]:
                s -= 1
        if s != line:
            return False
    return True


N, M, H = map(int, input().split())
ladders = [[0] * (N+1) for _ in range(H+1)]
result = 4
for _ in range(M):
    a, b = map(int, input().split())
    ladders[a][b] = 1

ladder = sum(ladders[0])
construct(0, 1, 1)
if result == 4:
    result = -1

print(result)
