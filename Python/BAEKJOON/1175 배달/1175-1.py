from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
s1, s2 = 0, 0
cnt = -1
find = False

for n in range(N):
    for m in range(M):
        if arr[n][m] == 'S':
            s1, s2 = n, m

q = deque([(s1, s2, 4, 0, set())])
while q:
    # print(visited)
    if find: break
    n, m, dd, c, delivery = q.popleft()
    for d in range(4):
        if d == dd or d == dd^1: continue
        nn, nm = n+di[d][0], m+di[d][1]
        if not (0 <= nn < N and 0 <= nm < M): continue
        if arr[nn][nm] == '#': continue
        if arr[nn][nm] == 'C': delivery.add((nn, nm))
        if len(delivery) == 2: find = True; cnt = c+1; break
        q.append((nn, nm, d, c+1, delivery))

print(cnt)
