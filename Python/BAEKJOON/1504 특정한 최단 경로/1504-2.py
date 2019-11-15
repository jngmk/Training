# 다익스트라
from heapq import heappop, heappush

N, E = map(int, input().split())
INF = float('inf')
arr = [[] for _ in range(N)]
dists = [INF] * N
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a-1].append([c, b-1])
    arr[b-1].append([c, a-1])

q = [[0, 0]]
while q:
    dist, n = heappop(q)
    for d, v in arr[n]:
        if dists[v] <= dist+d: continue
        dists[v] = dist+d
        heappush(q, [dist+d, v])

print(dists[n])

