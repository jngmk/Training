from collections import deque

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]
di = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque([[0, 0, 0]])  # pos, time
visited[0][0] = 1
save = False
time_limit = T
while q:
    n, m, t = q.popleft()

    if t >= time_limit: break

    for dn, dm in di:
        nn, nm = n+dn, m+dm
        if not (0 <= nn < N and 0 <= nm < M): continue
        if visited[nn][nm]: continue
        if arr[nn][nm] == 1: continue
        visited[nn][nm] = 1

        # meet sword
        if arr[nn][nm] == 2:
            tmp_t = t + 1 + abs(N-1-nn) + abs(M-1-nm)
            if tmp_t > T: break
            time_limit = tmp_t
            save = True
            continue

        # meet princess
        if (nn, nm) == (N-1, M-1):
            time_limit = t+1
            save = True
            continue

        # move
        q.append([nn, nm, t+1])

print(time_limit if save else 'Fail')
