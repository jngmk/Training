R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

water = []
beaver = [0, 0]
dochi = []

for r in range(R):
    for c in range(C):
        if board[r][c] == '*': water.append([r, c])
        elif board[r][c] == 'D': beaver = [r, c]
        elif board[r][c] == 'S': dochi = [[r, c]]

cnt = 0
ans = 'KAKTUS'
find = False
while water or dochi:
    if find: ans = cnt; break
    w, q = water, dochi
    water, dochi = [], []

    while w:
        wr, wc = w.pop()
        for dr, dc in (-1, 0), (1, 0), (0, 1), (0, -1):
            nwr, nwc = wr+dr, wc+dc
            if not (0 <= nwr < R and 0 <= nwc < C): continue
            if board[nwr][nwc] == 'X':
                continue
            elif board[nwr][nwc] == '*':
                continue
            elif board[nwr][nwc] == 'D':
                continue
            water.append([nwr, nwc])
            board[nwr][nwc] = '*'

    while q:
        r, c = q.pop()
        if find: break
        for dr, dc in (-1, 0), (1, 0), (0, 1), (0, -1):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C): continue
            if board[nr][nc] == 'X':
                continue
            elif board[nr][nc] == '*':
                continue
            elif board[nr][nc] == 'S':
                continue
            dochi.append([nr, nc])
            board[nr][nc] = 'S'
            if [nr, nc] == beaver:
                find = True
                break

    cnt += 1

print(ans)
