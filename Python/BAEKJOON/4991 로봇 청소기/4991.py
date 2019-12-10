from collections import deque
INF = float('inf')

while True:
    W, H = map(int, input().split())
    if W == 0: break
    arr = [list(input()) for _ in range(H)]
    r1, r2 = 0, 0
    messy_spaces = deque()
    m = 1

    # 배열 정리
    for h in range(H):
        for w in range(W):
            if arr[h][w] == '.': arr[h][w] = 0
            elif arr[h][w] == 'x': arr[h][w] = -1
            elif arr[h][w] == 'o':
                arr[h][w] = 1
                r1, r2 = h, w
                messy_spaces.appendleft([r1, r2])
            if arr[h][w] == '*':
                m += 1
                arr[h][w] = m
                messy_spaces.append([h, w])

    # 거리 측정
    distances = [[INF] * m for _ in range(m)]
    for h, w in messy_spaces:
        q = deque([[h, w, 0]])
        visit = arr[h][w]
        while q:
            a, b, cnt = q.popleft()
            for da, db in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                va, vb = a+da, b+db
                if not (0 <= va < H and 0 <= vb < W): continue
                if arr[va][vb] == -1 or arr[va][vb] == visit: continue
                if arr[va][vb] > visit:
                    if distances[visit-1][arr[va][vb]-1] != INF:
                        continue
                    distances[visit-1][arr[va][vb]-1] = cnt+1
                    distances[arr[va][vb]-1][visit-1] = cnt+1
                    q.append([va, vb, cnt + 1])
                    continue
                arr[va][vb] = visit
                q.append([va, vb, cnt+1])

    # 최단 거리
    min_dis = INF
    def perm(k, dis, visited):
        global min_dis
        if dis >= min_dis: return
        if k == m-1:
            min_dis = min(min_dis, dis)
            return
        else:
            for j in range(1, m):
                if j in visited: continue
                perm(k+1, dis+distances[visited[-1]][j], visited+[j])
    perm(0, 0, [0])
    print(min_dis if min_dis != INF else -1)
