from heapq import heappop, heappush

N, M = map(int, input().split())
metro = [0] * N
for n in range(N):
    m = int(input())
    metro[n] = m
arr = [list(map(int, input().split())) for _ in range(N)]

dis = [[0, 0, 0]]  # 환승횟수, 소요시간, 지하철역
visited = [0] * N

while True:
    t, c, m = heappop(dis)

    if visited[m]: continue
    visited[m] = 1

    if m == M:
        print('{} {}'.format(t, c))
        break

    for i in range(N):
        if visited[i]: continue
        if arr[m][i] > 0:
            if metro[m] == metro[i]:
                heappush(dis, [t, c+arr[m][i], i])
            else:
                heappush(dis, [t+1, c+arr[m][i], i])
