from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
houses, bhcs = [], []
for a in range(N):
    for b in range(N):
        if arr[a][b] == 1:
            houses.append((a, b))
        elif arr[a][b] == 2:
            bhcs.append((a, b))

dists = [[0] * len(houses) for _ in range(len(bhcs))]
min_dist = float('inf')
for r in range(len(bhcs)):
    a, b = bhcs[r]
    for c in range(len(houses)):
        d, e = houses[c]
        dists[r][c] = abs(a-d) + abs(b-e)

for survived_bhc in combinations(range(len(bhcs)), M):
    dist = 0
    for house in range(len(houses)):
        if dist >= min_dist: break
        tmp = float('inf')
        for bhc in range(len(bhcs)):
            if bhc not in survived_bhc: continue
            tmp = min(tmp, dists[bhc][house])
        dist += tmp
    min_dist = min(min_dist, dist)

print(min_dist)