from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
visited = [[[INF, INF] for _ in range(N)] for _ in range(N)]
visited[0][0][1] = 0
day = 1
convert = {0: 'moon', 1: 'sun '}
q = deque([(0, 0, 0, day)])
find = False
ans = -1
while q:
    for vis in visited:
        print(vis)
    if find: break
    r, c, cnt, day = q.popleft()
    if day:
        print(cnt, 'day')
        print()
        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            if board[nr][nc] == 1: continue
            tmp_day = 0 if cnt % M == 0 else 1
            if cnt + 1 >= visited[nr][nc][tmp_day]: continue
            if (nr, nc) == (N-1, N-1):
                print('arrived cnt', cnt)
                find = True; ans = str(cnt//(2 * M)) + ' ' + convert[tmp_day]
                break
            visited[nr][nc][tmp_day] = cnt + 1
            q.append((nr, nc, cnt+1, tmp_day))
    else:
        print(cnt, 'night')
        print()
        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
            rr, cc = r, c
            possible = False
            while True:
                nr, nc = rr + dr, cc + dc
                if not (0 <= nr < N and 0 <= nc < N): break
                if board[nr][nc] == 0: possible = True; break
                rr, cc = nr, nc
            if not possible: continue
            tmp_day = 1 if cnt % M == 0 else 0
            if cnt + 1 >= visited[nr][nc][tmp_day]: continue
            if (nr, nc) == (N-1, N-1):
                print('arrived cnt', cnt)
                find = True; ans = str(cnt//(2 * M)) + ' ' + convert[tmp_day]
                break
            visited[nr][nc][tmp_day] = cnt + 1
            q.append((nr, nc, cnt+1, tmp_day))

print(ans)
