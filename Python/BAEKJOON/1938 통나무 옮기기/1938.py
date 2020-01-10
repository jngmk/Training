import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
visited = [[[-1, -1] for _ in range(N)] for _ in range(N)]
B, E = [], []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'B':
            B.append((r, c))
        elif arr[r][c] == 'E':
            E.append((r, c))

b1, b2, b3 = 0, 0, 0
e1, e2, e3 = 0, 0, 0
if B[1][0] - B[0][0] == 0:  # 나무가 가로
    b1, b2, b3 = B[1][0], B[1][1], 0
    visited[b1][b2][0] = 0
else:
    b1, b2, b3 = B[1][0], B[1][1], 1
    visited[b1][b2][1] = 0

if E[1][0] - E[0][0] == 0:  # 나무가 가로
    e1, e2, e3 = E[1][0], E[1][1], 0
else:
    e1, e2, e3 = E[1][0], E[1][1], 1

q = deque([(b1, b2, b3, 0)])
find = False
while q:
    r, c, s, d = q.popleft()
    if visited[e1][e2][e3] >= 0: find = True; break
    if s == 0:  # 가로
        space = 0
        for dr, dc in (-1, 0), (1, 0):  # 상 하
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 1 <= nc < N-1): continue
            if arr[nr][nc] == '1': continue
            if arr[nr][nc-1] == '1' or arr[nr][nc+1] == '1': continue
            if visited[nr][nc][s] < 0:
                q.append((nr, nc, s, d+1))
                visited[nr][nc][s] = d+1
            space += 1

        if space == 2 and visited[r][c][1] < 0:  # 턴
            q.append((r, c, 1, d+1))
            visited[r][c][1] = d+1

        nr, nc = r, c-1  # 좌
        if nc-1 >= 0:
            if arr[nr][nc-1] != '1':
                if visited[nr][nc][s] < 0:
                    q.append((nr, nc, s, d+1))
                    visited[nr][nc][s] = d+1

        nr, nc = r, c+1  # 우
        if nc+1 < N:
            if arr[nr][nc+1] != '1':
                if visited[nr][nc][s] < 0:
                    q.append((nr, nc, s, d+1))
                    visited[nr][nc][s] = d+1
    else:
        space = 0
        for dr, dc in (0, -1), (0, 1):  # 좌 우
            nr, nc = r + dr, c + dc
            if not (1 <= nr < N-1 and 0 <= nc < N): continue
            if arr[nr][nc] == '1': continue
            if arr[nr-1][nc] == '1' or arr[nr+1][nc] == '1': continue
            if visited[nr][nc][s] < 0:
                visited[nr][nc][s] = d+1
                q.append((nr, nc, s, d+1))
            space += 1

        if space == 2 and visited[r][c][0] < 0:  # 턴
            q.append((r, c, 0, d+1))
            visited[r][c][0] = d+1

        nr, nc = r-1, c  # 상
        if nr-1 >= 0:
            if arr[nr-1][nc] != '1':
                if visited[nr][nc][s] < 0:
                    q.append((nr, nc, s, d+1))
                    visited[nr][nc][s] = d+1

        nr, nc = r+1, c  # 하
        if nr+1 < N:
            if arr[nr+1][nc] != '1':
                if visited[nr][nc][s] < 0:
                    q.append((nr, nc, s, d+1))
                    visited[nr][nc][s] = d+1

print(visited[e1][e2][e3] if find else 0)
