# 조합 부분집합을 구하면서 dfs 사용
virus = []
blanks = []
wall1 = []
N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
ans = 999999


def comb(k, now, temp):
    global ans
    if k == 3:
        result = counting(temp)
        if result[0] < ans:
            ans = result[0]
            wall = result[1]
    else:
        for i in range(now+1, len(blanks)):
            comb(k+1, i, temp + [blanks[i]])


for a in range(N):
    for b in range(M):
        if array[a][b] == 0:
            blanks.append((a, b))
        elif array[a][b] == 2:
            virus.append((a, b))
        elif array[a][b] == 1:
            wall1.append((a, b))


comb(0, -1, [])


def counting(temp):
    wall = []
    for aa, bb in temp:
        array[aa][bb] = 1
        wall.append((aa, bb))

    cnt = 0
    da = [-1, 0, 1, 0]
    db = [0, 1, 0, -1]
    is_visited = [[0] * M for _ in range(N)]
    top = -1
    stack = [0] * N * M
    for x, y in virus:
        stack[top+1] = x, y
        top += 1
    while top != -1:
        v1, v2 = stack[top]
        top -= 1
        cnt += 1
        for d in range(4):
            if 0 <= v1 + da[d] < N and 0 <= v2 + db[d] < M:
                if array[v1 + da[d]][v2 + db[d]] == 0 and not is_visited[v1 + da[d]][v2 + db[d]]:
                    stack[top + 1] = v1 + da[d], v2 + db[d]
                    top += 1
                    is_visited[v1 + da[d]][v2 + db[d]] = 1
    for aa, bb in temp:
        array[aa][bb] = 0

    return cnt, wall

print(ans)
