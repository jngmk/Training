# 플로이드 워샬, 시간초과
N, E = map(int, input().split())
INF = float('inf')
arr = [[INF] * N for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = c
    arr[b-1][a-1] = c
a, b = map(int, input().split())
a, b = a-1, b-1

for k in range(N):
    for i in range(N):
        if k == i: continue
        for j in range(N):
            if j == k or j == i: continue
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

print(min((arr[0][a]+arr[a][b]+arr[b][N-1]), (arr[0][b]+arr[b][a]+arr[a][N-1])))