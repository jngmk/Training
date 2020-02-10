def find_friends(rr, cc, C):
    friends = 1
    friendsArr = [[rr, cc]]
    qq = [[rr, cc]]
    visited[rr][cc] = 1
    while qq:
        rr, cc = qq.pop(0)
        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
            nrr, ncc = rr+dr, cc+dc
            if not (0 <= nrr < 12 and 0 <= ncc < 6): continue
            if visited[nrr][ncc]: continue
            if board[nrr][ncc] == C:
                qq.append([nrr, ncc])
                visited[nrr][ncc] = 1
                friends += 1
                friendsArr.append([nrr, ncc])
    if friends >= 4:
        boomed.extend(friendsArr)


def sort_board():
    for cc in range(6):
        tmp = ['.'] * 12
        idx = 0
        for rr in range(11, -1, -1):
            if board[rr][cc] != '.':
                tmp[idx] = board[rr][cc]
                idx += 1
        for rr in range(11, -1, -1):
            board[rr][cc] = tmp[11-rr]


board = [list(input()) for _ in range(12)]
cnt = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    boomed = []
    for r in range(11, -1, -1):
        for c in range(6):
            if visited[r][c]: continue
            if board[r][c] != '.':
                find_friends(r, c, board[r][c])

    if not boomed: break
    for boom in boomed:
        r, c = boom
        board[r][c] = '.'
    boomed = []

    sort_board()
    cnt += 1

print(cnt)
