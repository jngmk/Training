from collections import deque
import sys
sys.stdin = open('input.txt')

connected = {
    1: [[1, 2, 5, 6], [1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5]],
    2: [[1, 2, 5, 6], [0], [1, 2, 4, 7], [0]],
    3: [[0], [1, 3, 6, 7], [0], [1, 3, 4, 5]],
    4: [[1, 2, 5, 6], [1, 3, 6, 7], [0], [0]],
    5: [[0], [1, 3, 6, 7], [1, 2, 4, 7], [0]],
    6: [[0], [0], [1, 2, 4, 7], [1, 3, 4, 5]],
    7: [[1, 2, 5, 6], [0], [0], [1, 3, 4, 5]]
}
da, db = [-1, 0, 1, 0], [0, 1, 0, -1]
for tc in range(1, int(input())+1):
    N, M, a, b, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[a][b] = 1
    q = deque()
    q.append([a, b, 1])
    result = 1
    while q:
        a, b, cnt = q.popleft()
        for d in range(4):
            va, vb = a+da[d], b+db[d]
            if not (0 <= va < N and 0 <= vb < M): continue
            if arr[va][vb] == 0: continue
            if visited[va][vb]: continue
            if arr[va][vb] not in connected[arr[a][b]][d]: continue
            if cnt+1 > L: continue
            # print(va, vb)
            q.append([va, vb, cnt+1])
            visited[va][vb] = 1
            result += 1
    print('#{} {}'.format(tc, result))
    # break