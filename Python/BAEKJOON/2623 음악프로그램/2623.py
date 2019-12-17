import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0, []] for _ in range(N)]
for _ in range(M):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        arr[tmp[i]-1][1].append(tmp[i+1]-1)
        arr[tmp[i+1]-1][0] += 1

q = deque()
for i in range(N):
    if arr[i][0] == 0:
        q.append(i)

result = []
visited = [0] * N
while True:
    if not q:
        print(0)
        break
    v = q.popleft()
    visited[v] = 1
    result.append(v)
    if len(result) == N:
        for n in result: print(n+1)
        break
    for nv in arr[v][1]:
        arr[nv][0] -= 1
        if arr[nv][0] == 0 and not visited[nv]:
            q.append(nv)
