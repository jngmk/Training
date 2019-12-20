from heapq import heappop, heappush


def dijkstra(ss):
    global max_t
    for way in 0, 1:
        h = [[0, ss]]
        distances = [float('inf')] * N
        distances[ss] = 0
        cnt = N
        while cnt > 0:
            print(h)
            tt, v = heappop(h)
            if times[way][v] != -1: continue
            times[way][v] = tt
            max_t = max(max_t, times[0][v]+times[1][v])
            cnt -= 1
            for nv, dt in arr[v][way]:
                if times[way][nv] != -1: continue
                if distances[nv] <= dt: continue
                heappush(h, (tt+dt, nv))
                distances[nv] = dt


for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    times = [[-1] * N, [-1] * N]
    arr = [[[], []] for _ in range(N)]
    max_t = 0
    for _ in range(M):
        s, e, t = map(int, input().split())
        arr[s-1][1].append((e-1, t))
        arr[e-1][0].append((s-1, t))

    dijkstra(X-1)

    print('#{} {}'.format(tc, max_t))
