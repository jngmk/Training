import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    tmp = list(map(int, input().split()))
    arr = [[0] * N for _ in range(N)]
    indegrees = [0] * N
    for i in range(N-1):
        for j in range(i+1, N):
            arr[tmp[i]-1][tmp[j]-1] = 1
            indegrees[tmp[j]-1] += 1

    K = int(input())
    for _ in range(K):
        a, b = map(int, input().split())
        if arr[a-1][b-1] == 1:
            arr[a-1][b-1] = 0; arr[b-1][a-1] = 1
            indegrees[b-1] -= 1; indegrees[a-1] += 1
        else:
            arr[a-1][b-1] = 1; arr[b-1][a-1] = 0
            indegrees[b-1] += 1; indegrees[a-1] -= 1
    q, result = [], []
    for i in range(N):
        if indegrees[i] == 0:
            q.append(i)

    while True:
        if not q: print('IMPOSSIBLE'); break
        if len(q) > 1: print('?'); break
        v = q.pop(0)
        result.append(str(v+1))
        if len(result) == N: print(' '.join(result)); break
        for i in range(N):
            if arr[v][i] and indegrees[i]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    q.append(i)
