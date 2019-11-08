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
    for j, w in arr[v]:
        if v == j: continue
        if dists[j] <= dist+w: continue
        dists[j] = dist+w
        heappush(q, [dist+w, j])

dists[S-1] = 0
for i in range(V):
    print('INF' if dists[i] == INF else dists[i])