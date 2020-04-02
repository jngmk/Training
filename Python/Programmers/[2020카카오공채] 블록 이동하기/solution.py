from collections import deque


def solution(board):
    answer = 0
    N = len(board)
    visited = [[[0, 0] for _ in range(N)] for _ in range(N)]

    state = 0  # 0: 가로, 1: 세로
    bike = [[0, 0], [0, 1]]
    visited[0][0][0] = 1

    q = deque([[0, state, bike]])
    while q:
        cnt, s, bike = q.popleft()
        r, f = bike  # rear - front

        if f == [N-1, N-1]:
            answer = cnt
            break

        # move
        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
            r1, r2, f1, f2 = r[0] + dr, r[1] + dc, f[0] + dr, f[1] + dc
            if not (0 <= r1 and 0 <= r2 and f1 < N and f2 < N): continue
            if board[r1][r2] == 1 or board[f1][f2] == 1: continue
            if visited[r1][r2][s]: continue
            nxt = [[r1, r2], [f1, f2]]
            visited[r1][r2][s] = 1
            q.append([cnt+1, s, nxt])

        # rotate
        for dr, dc, s in (-1, 0, 0), (1, 0, 0), (0, -1, 1), (0, 1, 1):
            r1, r2, f1, f2 = r[0] + dr, r[1] + dc, f[0] + dr, f[1] + dc
            if s == 0 and not (0 <= r1 < N and 0 <= f1 < N): continue
            if s == 1 and not (0 <= r2 < N and 0 <= f2 < N): continue
            if board[r1][r2] == 1 or board[f1][f2] == 1: continue

            # 회전 후 rear 부분의 좌표
            rr1, rr2 = min(r1, r[0]), min(r2, r[1])
            if not (visited[rr1][rr2][s^1]):
                nxt = list(sorted([[r1, r2], [r[0], r[1]]]))
                visited[rr1][rr2][s^1] = 1
                q.append([cnt+1, s^1, nxt])

            ff1, ff2 = min(f1, f[0]), min(f2, f[1])
            if not (visited[ff1][ff2][s^1]):
                nxt = list(sorted([[f1, f2], [f[0], f[1]]]))
                visited[ff1][ff2][s^1] = 1
                q.append([cnt+1, s^1, nxt])

    return answer
