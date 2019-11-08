# 느림

from heapq import heappop, heappush

V, E = map(int, input().split())
S = int(input())
INF = float('inf')
arr = [[] for _ in range(V)]
dists = [INF] * V
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u-1].append([v-1, w])

q = [[0, S-1]]
while q:
    dist, v = heappop(q)
    if dists[v] != INF: continue
    dists[v] = dist
    for j, w in arr[v]:
        if dists[j] != INF: continue
        heappush(q, [dist+w, j])

for i in range(V):
    print('INF' if dists[i] == INF else dists[i])
