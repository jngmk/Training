# 런타임 에러
from heapq import heappop, heappush


def dijkstra(ss, way):
    h = [[0, ss]]
    cnt = N
    while cnt > 0:
        tt, v = heappop(h)
        if times[way][v] != -1: continue
        times[way][v] = tt
        cnt -= 1
        # print('h, way', h, way)
        # print('times', times[way])
        for nv in range(N):
            dt = arr[v][nv] if way == 1 else arr[nv][v]
            if dt == -1: continue
            if times[way][nv] != -1: continue
            # print('dt, nv', dt, nv)
            heappush(h, [tt+dt, nv])


for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    times = [[-1] * N, [-1] * N]
    arr = [[-1] * N for _ in range(N)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        arr[s-1][e-1] = t
    # for ar in arr:
    #     print(ar)
    # print()
    for i in 0, 1:
        dijkstra(X-1, i)

    max_t = 0
    for i in range(N):
        if i == X-1: continue
        max_t = max(max_t, times[0][i] + times[1][i])

    print('#{} {}'.format(tc, max_t))
