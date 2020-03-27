def select_soil(k, now, soil_idx):  # 배양액을 뿌릴 땅 선정
    if k == G + R:
        green_or_red(soil_idx, 0, 0, [])
    else:
        for s in range(now, S):
            select_soil(k+1, s+1, soil_idx + [s])


def green_or_red(soil_idx, k, now, temp):
    if k == G:
        green, red = [], []
        for i in range(G+R):
            if i in temp:
                green.append(soil[soil_idx[i]])
            else:
                red.append(soil[soil_idx[i]])
        solve(green, red)
    else:
        for s in range(now, G+R):
            green_or_red(soil_idx, k+1, s+1, temp + [s])


def solve(green, red):
    global max_flower

    flower = 0
    # 0: 호수, 1, 2: 퍼질 수 있는 땅, 3: green, 4: red
    copy = [board[n][:] for n in range(N)]
    for (n, m) in green:
        copy[n][m] = 3
    for (n, m) in red:
        copy[n][m] = 4

    # 초록색, 빨간색 순서로 진행
    while True:
        if not green or not red: break

        tmp_green = []
        while green:
            n, m = green.pop(0)
            # 녹색 배양액을 뿌렸었는데 꽃이 된 곳은 지나침
            if copy[n][m] == 0: continue
            copy[n][m] = 0
            for nn, nm in (0, -1), (0, 1), (1, 0), (-1, 0):
                vn, vm = n + nn, m+nm
                if not (0 <= vn < N and 0 <= vm < M): continue
                if copy[vn][vm] == 1 or copy[vn][vm] == 2:
                    tmp_green.append((vn, vm))
                    copy[vn][vm] = 3
        green = tmp_green

        tmp_red = []
        while red:
            n, m = red.pop(0)
            copy[n][m] = 0
            for nn, nm in (0, -1), (0, 1), (1, 0), (-1, 0):
                vn, vm = n + nn, m + nm
                if not (0 <= vn < N and 0 <= vm < M): continue
                if copy[vn][vm] == 1 or copy[vn][vm] == 2:
                    tmp_red.append((vn, vm))
                    copy[vn][vm] = 4
                elif copy[vn][vm] == 3:
                    copy[vn][vm] = 0
                    flower += 1
        red = tmp_red

    max_flower = max(flower, max_flower)


N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
soil = []

# 배양액 뿌릴 수 있는 땅
for n in range(N):
    for m in range(M):
        if board[n][m] == 2:
            soil.append((n, m))

S = len(soil)
max_flower = 0
select_soil(0, 0, [])

print(max_flower)