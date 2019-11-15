# 크루스칼
from heapq import heappush, heappop


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    px, py = find_set(x), find_set(y)
    if rank[px] == rank[py]:
        rank[py] += 1
    elif rank[px] > rank[py]:
        px, py = py, px
    p[px] = py


def indexing_island(aa, bb):
    global idx, ocean
    idx += 1
    q = [[aa, bb]]
    ocean[aa][bb] = idx
    while q:
        aa, bb = q.pop()
        for da, db in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            va, vb = aa+da, bb+db
            if not (0 <= va < N and 0 <= vb < M): continue
            if ocean[va][vb] != 1: continue
            ocean[va][vb] = idx
            q.append([va, vb])


def measure_dist(s, r, c):
    global dists
    visited = [[0] * M for _ in range(N)]
    q = [[r, c]]
    visited[r][c] = 1
    while q:
        r, c = q.pop()
        for da, db in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr, cc = r, c
            dist = -1
            while True:
                dist += 1
                va, vb = rr+da, cc+db
                if not (0 <= va < N and 0 <= vb < M): break
                if ocean[va][vb] == s:
                    if not visited[va][vb]:
                        q.append([va, vb])
                        visited[va][vb] = 1
                    break
                elif ocean[va][vb]:
                    if dist < 2: break
                    if dist < dists[s-1][ocean[va][vb]-1]:
                        dists[s-1][ocean[va][vb]-1] = dist
                        dists[ocean[va][vb]-1][s-1] = dist
                        heappush(h, [dist, s-1, ocean[va][vb]-1])
                    break
                rr, cc = va, vb


N, M = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
idx = 1
h = []

# 섬 넘버링
for a in range(N):
    for b in range(M):
        if ocean[a][b] == 1:
            indexing_island(a, b)

# 섬 최단거리
island_visited = [0] * idx
dists = [[INF] * idx for _ in range(idx)]  # 거리, 섬
for a in range(N):
    for b in range(M):
        if ocean[a][b] > 0 and not island_visited[ocean[a][b]-1]:
            measure_dist(ocean[a][b], a, b)
            island_visited[ocean[a][b]-1] = 1

# MST
bridge = 0
min_dist = 0
connected = [0] * (idx+1)
p = [i for i in range(idx+1)]
rank = [0] * (idx+1)
while h:
    if bridge == idx-2: break
    di, i1, i2 = heappop(h)
    if find_set(i1) == find_set(i2): continue
    union(i1, i2)
    bridge += 1
    min_dist += di

print(min_dist if bridge == idx-2 else -1)
