def solution(board):
    global flag, answer
    answer = 0
    flag = True
    while flag:
        board = fill(board)
        board = break_blocks(board)
    return answer


def fill(board):
    n = len(board)
    for c in range(n):
        for r in range(n):
            if not (0 < board[r][c] < 201):
                board[r][c] = 201
            else:
                break
    return board


def break_blocks(board):
    global visited, flag, answer
    flag = False
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    need_to_break = []
    for c in range(n):
        for r in range(n):
            if visited[r][c]: continue
            if 0 < board[r][c] < 201:
                blocks = check(board, r, c)
                if blocks:
                    need_to_break.extend(blocks)
                    answer += 1
                    flag = True
    for r, c in need_to_break:
        board[r][c] = 0
    return board


def check(board, r, c):
    global visited
    n = len(board)
    v = board[r][c]
    blocks = [[r, c]]
    q = [[r, c]]
    visited[r][c] = 1
    while q:
        r, c = q.pop(0)
        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < n): continue
            if visited[nr][nc]: continue
            if board[nr][nc] == v:
                q.append([nr, nc])
                visited[nr][nc] = 1
                blocks.append([nr, nc])

    min_r, max_r = n, 0
    min_c, max_c = n, 0
    for r, c in blocks:
        min_r = min(min_r, r)
        min_c = min(min_c, c)
        max_r = max(max_r, r)
        max_c = max(max_c, c)

    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if not (board[r][c] == v or board[r][c] == 201):
                return []
    return blocks


dataset = [
    [[10,10,10,0,0,0,0,0,0,0],
     [10,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,7,9,0,0,0,0,0],
     [0,0,0,7,9,9,9,0,0,0],
     [0,6,0,7,7,0,0,0,8,0],
     [0,6,0,0,3,0,0,8,8,8],
     [0,6,6,2,3,0,0,0,5,5],
     [1,2,2,2,3,3,0,0,0,5],
     [1,1,1,0,0,0,0,0,0,5]]
]

for board in dataset:
    print(solution(board))
