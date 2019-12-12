from heapq import heappush, heappop

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
INF = float('inf')
visited = [[INF for _ in range(M)] for _ in range(N)]
garbage = []
s1, s2 = 0, 0
di = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 배열 정리
for n in range(N):
    for m in range(M):
        if arr[n][m] == 'g':
            garbage.append([n, m])
            arr[n][m] = 2
        elif arr[n][m] == 'S':
            s1, s2 = n, m
            arr[n][m] = 4
        elif arr[n][m] == 'F': arr[n][m] = 3
        else: arr[n][m] = 0

while garbage:
    g1, g2 = garbage.pop()
    for dg1, dg2 in di:
        ng1, ng2 = g1+dg1, g2+dg2
        if not (0 <= ng1 < N and 0 <= ng2 < M): continue
        if arr[ng1][ng2] != 0: continue
        arr[ng1][ng2] = 1

# 탐색
angry, upset = 2500, 2500
visited[s1][s2] = 1
pos = [[0, 0, s1, s2]]  # angry, upset, pos
while pos:
    a, u, n, m = heappop(pos)

    if angry * 10000 + upset < a * 10000 + u: continue

    for dn, dm in di:
        nn, nm = n+dn, m+dm
        if not (0 <= nn < N and 0 <= nm < M): continue

        if arr[nn][nm] == 3:
            angry, upset = a, u
            continue

        aa, uu = a, u
        visit = aa * 10000 + uu + 1
        if arr[nn][nm] == 1: uu += 1
        elif arr[nn][nm] == 2: aa += 1
        if visited[nn][nm] <= visit: continue

        visited[nn][nm] = visit
        heappush(pos, [aa, uu, nn, nm])

print(angry, upset)
