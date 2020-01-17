import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
trails = [[] for _ in range(N+1)]
visited = [0] * (N+1)  # 가지고 온 짐의 크기

for _ in range(M):
    a, b, c = map(int, input().split())
    trails[a].append([-c, b])
    trails[b].append([-c, a])

s, e = map(int, input().split())
h = []
for trail in trails[s]:
    heappush(h, trail)  # 가지고 오는 짐의 크기, 다음 섬
    visited[trail[1]] = trail[0]

while True:
    w, v = heappop(h)
    if v == e: print(-w); break
    for nw, nv in trails[v]:  # 다리 중량, 다음 섬
        new_w = max(w, nw)  # 다리가 무게를 못 견딜때
        if visited[nv] <= new_w: continue
        heappush(h, [new_w, nv])
        visited[nv] = new_w
