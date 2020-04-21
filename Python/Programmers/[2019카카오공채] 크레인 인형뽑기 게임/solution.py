def solution(board, moves):
    N = len(board)
    answer = 0
    stack = [0] * len(moves)
    top = 0
    for c in moves:
        for r in range(N):
            if board[r][c-1] != 0:
                stack[top] = board[r][c-1]
                top += 1
                board[r][c-1] = 0
                break
        if top != 0 and top != 1 and stack[top-1] == stack[top-2]:
            stack[top-1], stack[top-2] = 0, 0
            top -= 2
            answer += 2
    return answer