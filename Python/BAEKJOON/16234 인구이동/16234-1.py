from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0

while True:
    immigration = False
    visited = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if visited[a][b]: continue
            visited[a][b] = 1
            q = deque()
            union = []
            population = 0
            group = 0
            for da, db in di:
                va, vb = a+da, b+db
                if not (0 <= va < N and 0 <= vb < N): continue
                if not (L <= abs(arr[va][vb] - arr[a][b]) <= R): continue
                q.append([a, b])
                immigration = True
                break
            while q:
                # print(q)
                aa, bb = q.popleft()
                # print(aa, bb)
                union.append([aa, bb])
                population += arr[aa][bb]
                group += 1
                for da, db in di:
                    va, vb = aa + da, bb + db
                    # print(va, vb)
                    if not (0 <= va < N and 0 <= vb < N): continue
                    if visited[va][vb]: continue
                    # print(abs(arr[va][vb] - arr[aa][bb]))
                    if not (L <= abs(arr[va][vb] - arr[aa][bb]) <= R): continue
                    q.append([va, vb])
                    visited[va][vb] = 1
            if group:
                # print(group)
                new_pop = population // group
                for ua, ub in union:
                    arr[ua][ub] = new_pop
    # print(arr)
    if not immigration: break
    cnt += 1

print(cnt)