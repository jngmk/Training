N, K, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    tmp = list(map(int, input().split()))
    for t in tmp:
        for tt in tmp:
            if t == tt: continue
            arr[t-1].append(tt-1)
# print(arr)
q = [[0, 1]]
while True:
    v, cnt = q.pop(0)
    if v == N-1:
        print(cnt)
        break
    for nxt in arr[v]:
        q.append([nxt, cnt+1])
