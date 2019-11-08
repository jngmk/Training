from itertools import combinations
from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
da, db = [0, 0, -1, 1], [-1, 1, 0, 0]
blanks = 0
viruses = []
times = N * N
for a in range(N):
    for b in range(N):
        if arr[a][b] == 2:
            viruses.append([a, b])
        elif arr[a][b] == 0:
            blanks += 1

orders = list(combinations(range(len(viruses)), M))

for order in orders:
    q = deque()
    infected = 0
    visited = [[0] * N for _ in range(N)]
    for idx in order:
        q.append(viruses[idx]+[0])

    while q:
        a, b, cnt = q.popleft()
        if cnt >= times:
            break
        for d in range(4):
            va, vb = a+da[d], b+db[d]
            if not (0 <= va < N and 0 <= vb < N):
                continue
            if arr[va][vb] == 2 and visited[va][vb] == 0:
                q.append([va, vb, cnt + 1])
                visited[va][vb] = 1
            if arr[va][vb] == 0 and visited[va][vb] == 0:
                q.append([va, vb, cnt+1])
                visited[va][vb] = 1
                infected += 1
                if infected == blanks:
                    times = min(times, cnt+1)
                    break
        if infected == blanks:
            break

print(0 if blanks == 0 else (-1 if times == N * N else times))
