from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[[0] * 3 for _ in range(4)] for _ in range(M)] for _ in range(N)]  # 5차원배열
s1, s2 = 0, 0
cnt = -1
find = False
C = dict()

tmp = 1
for n in range(N):
    for m in range(M):
        if arr[n][m] == 'S':
            s1, s2 = n, m
        elif arr[n][m] == 'C':
            arr[n][m] = tmp
            tmp += 1

q = deque([(s1, s2, 4, 0, 0)])  # 위치, 왔던 방향, 카운트, 배달
while q:
    if find: break
    n, m, dd, c, delivery = q.popleft()
    for d in range(4):
        if d == dd: continue
        delivery1 = delivery
        nn, nm = n+di[d][0], m+di[d][1]
        if not (0 <= nn < N and 0 <= nm < M): continue
        if arr[nn][nm] == '#': continue
        if visited[nn][nm][d][delivery1]: continue
        if arr[nn][nm] == 1 or arr[nn][nm] == 2:
            if delivery1 == 0:
                delivery1 = arr[nn][nm]
            elif delivery1 != arr[nn][nm]:
                find = True; cnt = c+1; break
        q.append((nn, nm, d, c+1, delivery1))
        visited[nn][nm][d][delivery1] = 1

print(cnt)
