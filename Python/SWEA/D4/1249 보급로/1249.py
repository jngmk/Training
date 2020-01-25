from heapq import heappush, heappop

T = int(input())
INF = float('inf')
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(str(input())))) for _ in range(N)]
    s1, s2, e1, e2 = 0, 0, N-1, N-1
    visited = [[INF] * N for _ in range(N)]
    q = []
    heappush(q, [board[s1][s2], s1, s2])
    visited[s1][s2] = board[s1][s2]

    find = False
    ans = 0
    while q:
        if find: break
        cost, r, c = heappop(q)
        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
            nr, nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            ncost = cost+board[nr][nc]
            if (nr, nc) == (e1, e2):
                ans = ncost; find = True
                break
            if ncost >= visited[nr][nc]: continue
            heappush(q, [ncost, nr, nc])
            visited[nr][nc] = ncost

    print('#{} {}'.format(tc, ans))
