from heapq import heappop, heappush

da, db = [0, 0, -1, 1], [-1, 1, 0, 0]
INF = float('inf')
tc = 1
while True:
    N = int(input())
    if N == 0: break
    arr = [list(map(int, input().split())) for _ in range(N)]
    rupee = [[INF] * N for _ in range(N)]
    S, G = [0, 0], [N-1, N-1]
    h = []
    heappush(h, [arr[0][0], 0, 0])
    while h:
        r, a, b = heappop(h)
        rupee[a][b] = r
        if [a, b] == G: break
        for d in range(4):
            va, vb = a+da[d], b+db[d]
            if not (0 <= va < N and 0 <= vb < N): continue
            if rupee[va][vb] <= arr[va][vb] + r: continue
            rupee[va][vb] = arr[va][vb] + r
            heappush(h, [arr[va][vb] + r, va, vb])
    print('Problem {}: {}'.format(tc, r))
    tc += 1
