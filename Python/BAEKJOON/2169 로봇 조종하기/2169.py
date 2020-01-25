def go_right(n, m):
    global dp
    while True:
        if m + 1 >= M: break
        if dp[n][m+1][0] <= dp[n][m][0] + dp[n][m+1][2]:
            dp[n][m+1][0] = dp[n][m][0] + dp[n][m+1][2]
        else: return
        m += 1


def go_left(n, m):
    global dp
    while True:
        if m - 1 < 0: break
        if dp[n][m-1][1] <= dp[n][m][1] + dp[n][m-1][2]:
            dp[n][m-1][1] = dp[n][m][1] + dp[n][m-1][2]
        else: return
        m -= 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-float('inf') for _ in range(3)] for _ in range(M)] for _ in range(N)]  # from left, right, up
for n in range(N):
    for m in range(M):
        dp[n][m][2] = board[n][m]
dp[0][0], dp[N-1][M-1] = [board[0][0]] * 3, [board[N-1][M-1]] * 3

# 첫번째 줄
go_right(0, 0)

# 위에서 한 줄씩 진행
for n in range(1, N):
    # 위에서 아래로 진행
    for m in range(M):
        value = max(dp[n-1][m])+dp[n][m][2]
        dp[n][m][0], dp[n][m][1] = value, value
    for v in dp:
        print(v)
    print()
    for m in range(M):
        print(n, m)
        go_right(n, m)
        go_left(n, m)
        for v in dp:
            print(v)

print(max(dp[N-1][M-1]))