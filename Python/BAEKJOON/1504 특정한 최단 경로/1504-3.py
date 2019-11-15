# 다익스트라
from heapq import heappop, heappush


def dijkstra(s, g):
    global dists
    for i in range(N):
        if i == s: continue
        dists[i] = INF
    h = [[dists[s], s]]
    while h:
        dist, n = heappop(h)
        if dist > dists[n]: continue
        if n == g:
            return True
        for d, v in arr[n]:
            if dist+d >= dists[v]: continue
            dists[v] = dist+d
            heappush(h, [dist+d, v])
    return False


N, E = map(int, input().split())
INF = float('inf')
arr = [[] for _ in range(N)]
visited = [0] * N
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a-1].append([c, b-1])
    arr[b-1].append([c, a-1])
n1, n2 = map(int, input().split())
n1 -= 1; n2 -=1

dists = [INF] * N
dists[0] = 0
dist1 = dist2 = INF
if dijkstra(0, n1):
    if dijkstra(n1, n2):
        if dijkstra(n2, N-1):
            dist1 = dists[N-1]
dists = [INF] * N
dists[0] = 0
if dijkstra(0, n2):
    if dijkstra(n2, n1):
        if dijkstra(n1, N-1):
            dist2 = dists[N-1]
print(-1 if min(dist1, dist2) == INF else min(dist1, dist2))
