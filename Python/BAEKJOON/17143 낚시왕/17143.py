# 시간초과
R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
xx = [0, -1, 1, 0, 0]
yy = [0, 0, 0, 1, -1]
gotcha = 0
beaten = []


def is_wall():
    global r, c, d
    if r == 1 and d == 1:
        d += 1
    elif r == R and d == 2:
        d -= 1
    elif c == 1 and d == 4:
        d -= 1
    elif c == C and d == 3:
        d += 1


for person in range(1, C+1):
    print(sharks)
    # person 의 위치와 가장 가까운 상어 포획
    min_r = R+1
    for shark in range(len(sharks)):
        r, c, s, d, z = sharks[shark]
        if c == person:
            if min_r > r:
                min_r = r
                idx = shark
        # 상어 이동
        for _ in range(s):
            r, c, s, d, z = sharks[shark]
            is_wall()
            dx = xx[d]
            dy = yy[d]
            sharks[shark] = [r + dx, c + dy, s, d, z]
            print(sharks)
    if min_r < R+1:
        gotcha += sharks[idx][4]
        sharks.pop(idx)

    # 상어 포식
    position = {}
    for shark in range(len(sharks)):
        r, c = sharks[shark][0], sharks[shark][1]
        if position.get((r, c)):
            position.get((r, c)).append(shark)
        else:
            position.update({(r, c): [shark]})

    position = sorted(position.values())
    for p in position:
        if len(p) > 1:
            biggest = sharks[p[0]][4]
            big_idx = p[0]
            for pp in range(1, len(p)):
                if sharks[p[pp]][4] > biggest:
                    beaten.append(big_idx)
                    biggest = sharks[p[pp]][4]
                    big_idx = p[pp]
                else:
                    beaten.append(p[pp])

    beaten = sorted(beaten)
    while beaten:
        sharks.pop(beaten.pop())

    print(gotcha)

print(gotcha)
