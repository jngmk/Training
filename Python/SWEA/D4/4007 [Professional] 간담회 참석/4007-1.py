# 시간초과
INF = float('inf')

for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    arr = [[INF] * N for _ in range(N)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        arr[s-1][e-1] = t
    # for ar in arr:
    #     print(ar)
    # print()
    for k in range(N):
        for x in range(N):
            if k == x: continue
            for y in range(N):
                if k == y or x == y: continue
                # if arr[x][k] == INF or arr[k][y] == INF: continue
                arr[x][y] = min(arr[x][y], arr[x][k]+arr[k][y])
    # for ar in arr:
    #     print(ar)
    # print()
    max_t = 0
    for i in range(N):
        if i == X-1: continue
        time = arr[i][X-1] + arr[X-1][i]
        max_t = max(max_t, time)

    print('#{} {}'.format(tc, max_t))
