N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
s1, s2 = 0, 0
size = 2
time = 0
cnt = 0
eat = 0

for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            s1, s2 = r, c
            board[s1][s2] = 0

q = [[-cnt, time, s1, s2, eat, size]]

# 잡아먹으면 qq을 교체
while q:
    find = 0
    find_sharks = []
    visited = [[0] * N for _ in range(N)]
    item = q.pop(0)
    visited[item[2]][item[3]] = item[5]
    qq = [item[:]]
    while qq:
        cnt, time, r, c, eat, size = qq.pop(0)
        if find != 0 and find == time:
            cnt, time, r, c, eat, size = list(sorted(find_sharks))[0]
            q.append([cnt, time, r, c, eat, size])
            board[r][c] = 0
            break
        for dr, dc in (-1, 0), (0, -1), (1, 0), (0, 1):
            nr, nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            if visited[nr][nc] == size: continue
            if board[nr][nc] == size or board[nr][nc] == 0:
                qq.append([cnt, time+1, nr, nc, eat, size])
                visited[nr][nc] = size
            elif board[nr][nc] < size:
                if eat+1 == size:
                    find_sharks.append([cnt-1, time+1, nr, nc, 0, size+1])
                    qq.append([cnt-1, time+1, nr, nc, 0, size+1])
                else:
                    find_sharks.append([cnt-1, time+1, nr, nc, eat+1, size])
                    qq.append([cnt-1, time+1, nr, nc, eat+1, size])
                visited[nr][nc] = size
                find = time+1

print(item[1])
