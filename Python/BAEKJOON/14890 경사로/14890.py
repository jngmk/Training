def down1(a, b):
    global n, tmp
    for _ in range(L-1):
        if b+1 < N:
            if arr[a][b+1] == h:
                n += 1
                b += 1
                tmp[b] = 1
            else:
                return False
        else:
            return False
    return True


def down2(a, b):
    global n, tmp
    for _ in range(L-1):
        if a+1 < N:
            if arr[a+1][b] == h:
                n += 1
                a += 1
                tmp[a] = 1
            else:
                return False
        else:
            return False
    return True


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 가로
for r in range(N):
    h = arr[r][0]  # 경사
    n = 1  # 평탄한 길 길이
    flag = True
    tmp = [0] * N
    for c in range(1, N):
        # 내려가는 경사로를 놓았다면
        if tmp[c]:
            h = arr[r][c]
            continue
        # 다음 칸이 경사가 없다면
        if arr[r][c] == h:
            n += 1
        # 높아지는 경사
        elif arr[r][c] == h+1:
            if n >= L:  # 경사로를 놓기 충분
                h = arr[r][c]
                n = 1
            else:
                flag = False
                continue
        # 낮아지는 경사
        elif arr[r][c] == h-1:
            h = arr[r][c]
            tmp[c] = 1
            n = 1
            if down1(r, c):
                n = 0
            else:
                flag = False
                continue
        # 터무니 없는 경사
        else:
            flag = False
            continue
    # print(tmp)
    if flag:
        # print(1, r, c)
        result += 1

# 세로
for c in range(N):
    h = arr[0][c]  # 경사
    n = 1  # 평탄한 길 길이
    flag = True
    tmp = [0] * N
    for r in range(1, N):
        # 내려가는 경사로를 놓았다면
        if tmp[r]:
            h = arr[r][c]
            continue
        # 다음 칸이 경사가 없다면
        if arr[r][c] == h:
            n += 1
        # 높아지는 경사
        elif arr[r][c] == h+1:
            if n >= L:  # 경사로를 놓기 충분
                h = arr[r][c]
                n = 1
            else:
                flag = False
                continue
        # 낮아지는 경사
        elif arr[r][c] == h-1:
            h = arr[r][c]
            tmp[r] = 1
            n = 1
            if down2(r, c):
                n = 0
            else:
                flag = False
                continue
        # 터무니 없는 경사
        else:
            flag = False
            continue
    # print(tmp)
    if flag:
        # print(2, r, c)
        result += 1

print(result)
