from collections import deque
import sys
sys.stdin = open('input.txt')

di8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    mines = []
    num_total = 0
    trying = 0
    for a in range(N):
        for b in range(N):
            if arr[a][b] == '.': arr[a][b] = 0
            elif arr[a][b] == '*': mines.append((a, b))

    # 주변 지뢰 개수 체크
    for a, b in mines:
        for da, db in di8:
            va, vb = a+da, b+db
            if not (0 <= va < N and 0 <= vb < N): continue
            if arr[va][vb] != '*': arr[va][vb] += 1

    # 0 눌러서 최소횟수로 숫자 개방
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 0 and not visited[a][b]:
                q = deque([[a, b]])
                num_total += 1
                trying += 1
                visited[a][b] = 1
                while q:
                    aa, bb = q.popleft()
                    for da, db in di8:
                        va, vb = aa+da, bb+db
                        if not (0 <= va < N and 0 <= vb < N): continue
                        if visited[va][vb]: continue
                        if arr[va][vb] != '*': visited[va][vb] = 1; num_total += 1
                        if arr[va][vb] == 0: q.append([va, vb])

    print('#{} {}'.format(tc, trying+(N*N-len(mines)-num_total)))
