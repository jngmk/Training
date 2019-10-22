def block1(a, b):
    global result
    if not (0 <= a < N and 0 <= b+3 < M):
        return
    tmp = arr[a][b] + arr[a][b+1] + arr[a][b+2] + arr[a][b+3]
    result = max(result, tmp)


def block2(a, b):
    global result
    if not (0 <= a+3 < N and 0 <= b < M):
        return
    tmp = arr[a][b] + arr[a+1][b] + arr[a+2][b] + arr[a+3][b]
    result = max(result, tmp)


def block3(a, b):
    global result
    if 0 <= a+2 < N and 0 <= b+1 < M:
        tmp = arr[a][b] + arr[a+1][b] + arr[a+2][b]
        result = max(result, tmp + arr[a+2][b+1], tmp + arr[a][b+1], tmp + arr[a+1][b+1])

    if 0 <= a+2 < N and 0 <= b-1 < M:
        tmp = arr[a][b] + arr[a + 1][b] + arr[a + 2][b]
        result = max(result, tmp + arr[a+2][b-1], tmp + arr[a][b-1], tmp + arr[a+1][b-1])


def block4(a, b):
    global result
    if 0 <= a+1 < N and 0 <= b+2 < M:
        tmp = arr[a][b] + arr[a][b+1] + arr[a][b+2]
        result = max(result, tmp + arr[a+1][b], tmp + arr[a+1][b+2], tmp + arr[a+1][b+1])

    if 0 <= a-1 < N and 0 <= b+2 < M:
        tmp = arr[a][b] + arr[a][b + 1] + arr[a][b + 2]
        result = max(result, tmp + arr[a-1][b], tmp + arr[a-1][b+2], tmp + arr[a-1][b+1])


def block5(a, b):
    global result
    if not (0 <= a+2 < N and 0 <= b+1 < M):
        return
    tmp = arr[a+1][b] + arr[a+1][b+1]
    result = max(result, tmp + arr[a][b] + arr[a+2][b+1], tmp + arr[a][b+1] + arr[a+2][b])


def block6(a, b):
    global result
    if not (0 <= a+1 < N and 0 <= b+2 < M):
        return
    tmp = arr[a][b+1] + arr[a+1][b+1]
    result = max(result, tmp + arr[a][b] + arr[a+1][b+2], tmp + arr[a+1][b] + arr[a][b+2])


def block7(a, b):
    global result
    tmp = 0
    if not (0 <= a+1 < N and 0 <= b+1 < M):
        return
    tmp += arr[a][b] + arr[a+1][b] + arr[a][b+1] + arr[a+1][b+1]
    result = max(result, tmp)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        block1(i, j)
        block2(i, j)
        block3(i, j)
        block4(i, j)
        block5(i, j)
        block6(i, j)
        block7(i, j)
print(result)

