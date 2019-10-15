da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
N = int(input())
arr = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 2
L = int(input())
changes = []
for _ in range(L):
    x, y = map(str, input().split())
    y = 1 if y == 'D' else -1
    changes.append((int(x), y))

t1, t2 = 0, 0
h1, h2 = 0, 0
d = 1
arr[0][0] = [1, d]
flag = True
cnt = 0
while True:
    cnt += 1
    if flag and changes:
        second, direction = changes.pop(0)
        flag = False

    if cnt == second:
        d = (d + direction) % 4
        flag = True

    # 이동
    h_d = arr[h1][h2][1]
    t_d = arr[t1][t2][1]
    h1 += da[h_d]
    h2 += db[h_d]

    # 종료
    if h1 < 0 or h1 > N - 1 or h2 < 0 or h2 > N - 1:
        break
    if arr[h1][h2] != 0 and arr[h1][h2] != 2:
        if arr[h1][h2][0] == 1:
            break

    if arr[h1][h2] == 2:
        arr[h1][h2] = [1, d]
    else:
        arr[h1][h2] = [1, d]
        arr[t1][t2] = 0
        t1 += da[t_d]
        t2 += db[t_d]
print(cnt)
