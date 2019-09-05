# 조합 부분집합 구한 후 dfs 사용
virus = []
blanks = []
N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
ans = 999999
result = []


for a in range(N):
    for b in range(M):
        if array[a][b] == 0:
            blanks.append((a, b))
        elif array[a][b] == 2:
            virus.append((a, b))


def comb(k, now, temp):
    global result
    if k == 3:
        result.append(temp)
    else:
        for i in range(now+1, len(blanks)):
            comb(k+1, i, temp + [blanks[i]])


comb(0, -1, [])
for res in result:
    for aa, bb in res:
        array[aa][bb] = 1

    cnt = 0
    da = [-1, 0, 1, 0]
    db = [0, 1, 0, -1]
    is_visited = [[0] * M for _ in range(N)]
    top = -1
    stack = [0] * N * M
    for x, y in virus:
        stack[top+1] = x, y
        top += 1
        is_visited[x][y] = 1
    while top != -1:
        v1, v2 = stack[top]
        top -= 1
        cnt += 1
        for d in range(4):
            if 0 <= v1+da[d] < N and 0 <= v2+db[d] < M:
                if array[v1+da[d]][v2+db[d]] == 0 and not is_visited[v1+da[d]][v2+db[d]]:
                    stack[top+1] = v1+da[d], v2+db[d]
                    top += 1
                    is_visited[v1+da[d]][v2+db[d]] = 1
    for aa, bb in res:
        array[aa][bb] = 0

    if ans > cnt:
        ans = cnt
        res1 = res

result = len(blanks) - ans + len(virus) - 3
print(result)
