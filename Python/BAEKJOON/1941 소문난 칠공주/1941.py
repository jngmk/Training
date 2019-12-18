from itertools import combinations
from collections import deque

soms = [0] * 45
idx = 0
arr = [list(input()) for _ in range(5)]
princesses = []
result = 0
for i in range(5):
    for j in range(5):
        idx = 10 * i + j
        if arr[i][j] == 'S': soms[idx] = 1
        princesses.append(idx)

for comb in combinations(princesses, 7):
    som = 0
    for c in comb:
        if soms[c]: som += 1
    if som < 4: continue

    visited = dict()
    visited[comb[0]] = 1
    cnt = 1
    q = deque([comb[0]])
    possible = False
    while q:
        if possible: result += 1; break
        v = q.popleft()
        for d in (-1, 1, -10, 10):
            nv = v+d
            if visited.get(nv): continue
            if nv not in comb: continue
            visited[nv] = 1
            cnt += 1
            q.append(nv)
            if cnt == 7: possible = True; break

print(result)
