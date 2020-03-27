from heapq import heappop, heappush

N = int(input())
arr = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, c = map(int, input().split())
    arr[u].append((v, c))
    arr[v].append((u, c))

# for a in arr:
#     print(a)
# print()

min_cnt = float('inf')
h = []
visited = [[float('inf')] * N for _ in range(N)]
for n in range(N):
    visited_clone = visited[n][:]
    visited_clone[n] = 0
    for v, c in arr[n]:
        heappush(h, [c, v])

    while h:
        c, v = heappop(h)
        if visited_clone[v] < c: continue
        visited[v] = c
        for vv, cc in arr[v]:
            if visited_clone[vv] <= c + cc: continue
            visited_clone[vv] = c + cc
            heappush(h, [c + cc, vv])
    cnt = 0
    for i in range(N):
        visited[i][n] = visited_clone[i]
    min_cnt = min(min_cnt, sum(visited_clone))

print(min_cnt)