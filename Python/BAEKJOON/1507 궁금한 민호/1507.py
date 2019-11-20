N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
total = 0
for k in range(N):
    for i in range(N):
        if k == i: continue
        for j in range(N):
            if k == j or i == j: continue
            if arr[i][j] == arr[i][k] + arr[k][j]:
                visited[i][j] = 1

for i in range(N):
    for j in range(N):
        if visited[i][j]: continue
        total += arr[i][j]

for a in arr:
    print(a)
for a in visited:
    print(a)
print(total//2)
