from sys import stdin
input = stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    H = arr[i][0]
    cnt = 1
    for j in range(1, N):
        if H == arr[i][j]: pass
        elif H - arr[i][j] == 1:
            if cnt < 0: break
            H = arr[i][j]
            cnt = -L
        elif arr[i][j] - H == 1:
            if cnt < L: break
            H = arr[i][j]
            cnt = 0
        else: break
        cnt += 1
    else:
        if cnt > -1: ans += 1

for j in range(N):
    H = arr[0][j]
    cnt = 1
    for i in range(1, N):
        if H == arr[i][j]: pass
        elif H - arr[i][j] == 1:
            if cnt < 0: break
            H = arr[i][j]
            cnt = -L
        elif arr[i][j] - H == 1:
            if cnt < L: break
            H = arr[i][j]
            cnt = 0
        else: break
        cnt += 1
    else:
        if cnt > -1: ans += 1

print(ans)