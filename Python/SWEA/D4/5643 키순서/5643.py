from collections import deque
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = int(input()), int(input())
    arr = [[[], []] for _ in range(N)]  # 부모, 자식
    for _ in range(M):
        a, b = map(int, input().split())
        arr[b-1][1].append(a-1)
        arr[a-1][0].append(b-1)
    # print(arr)
    result = 0
    for i in range(N):
        visited = [0] * N
        q = deque()
        # 부모, 자식 확인
        for j in range(2):
            q.append(i)
            while q:
                # print(q)
                v = q.popleft()
                visited[v] = 1
                for k in arr[v][j]:
                    if not visited[k]:
                        q.append(k)
            # print(i, j, visited)

        if sum(visited) == N: result += 1
    print('#{} {}'.format(tc, result))