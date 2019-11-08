import heapq

N, M, X = map(int, input().split())
arr = [[99999999999999 for b in range(N)] for a in range(N)]
result = 0
for _ in range(M):
    a, b, d = map(int, input().split())
    arr[a-1][b-1] = d
# print(arr)

q = []
dists2 = [9999999999999999] * N
dists2[X-1] = 0
for j in range(N):
    dists2[j] = arr[X-1][j]
    if X-1 == j: continue
    heapq.heappush(q, [arr[X-1][j], j])
    dists2[j] = arr[X-1][j]
while q:
    # print(q)
    dist, v = heapq.heappop(q)
    # print(dist, v)
    for k in range(N):
        if dists2[k] <= dist+arr[v][k]: continue
        heapq.heappush(q, [dist+arr[v][k], k])
        dists2[k] = dist+arr[v][k]

for i in range(N):
    if i == X - 1: continue
    one_way = two_way = 0
    # print(i, '-----------------------------------')
    # one way
    q = []
    dists = [9999999999999999] * N
    dists[i] = 0
    for j in range(N):
        dists[j] = arr[i][j]
        if i == j: continue
        heapq.heappush(q, [arr[i][j], j])
        dists[j] = arr[i][j]
    while q:
        # print(q)
        dist, v = heapq.heappop(q)
        # print(dist, v)
        if v == X - 1:
            one_way = dist
            break
        for k in range(N):
            if dists[k] <= dist+arr[v][k]: continue
            heapq.heappush(q, [dist+arr[v][k], k])
            dists[k] = dist+arr[v][k]

    two_way = dists2[i]
    result = max(result, one_way+two_way)

print(result)
