R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
xx = [0, -1, 1, 0, 0]
yy = [0, 0, 0, 1, -1]
gotcha = 0
beaten = []


def moving(rr, cc, ss, dd, zz):  # c -1 로 모듈러
    if dd == 1:
        move = rr - 1
        if ss > move:
            sss = ss - move
            if sss >= R - 1:
                a, b = divmod(sss, R - 1)
                if a % 2 == 1:
                    rr = R - b
                else:
                    rr = 1 + b
                    dd = 2
            else:
                rr = 1 + sss
                dd = 2
        else:
            rr = rr - ss

    elif dd == 2:
        move = R - rr
        if ss > move:
            sss = ss - move
            if sss >= R - 1:
                a, b = divmod(sss, R - 1)
                if a % 2 == 1:
                    rr = 1 + b
                else:
                    rr = R - b
                    dd = 1
            else:
                rr = R - sss
                dd = 1
        else:
            rr = rr + ss

    elif dd == 3:
        move = C - cc
        if ss > move:
            sss = ss - move
            if sss >= C - 1:
                a, b = divmod(sss, C - 1)
                if a % 2 == 1:
                    cc = 1 + b
                else:
                    cc = C - b
                    dd = 4
            else:
                cc = C - sss
                dd = 4
        else:
            cc = cc + ss

    elif dd == 4:
        move = cc - 1
        if ss > move:
            sss = ss - move
            if sss >= C - 1:
                a, b = divmod(sss, C - 1)
                if a % 2 == 1:
                    cc = C - b
                else:
                    cc = 1 + b
                    dd = 3
            else:
                cc = 1 + sss
                dd = 3
        else:
            cc = cc - ss

    return [rr, cc, ss, dd, zz]


for person in range(1, C+1):
    # person 의 위치와 가장 가까운 상어 포획
    min_r = R+1
    for shark in range(len(sharks)):
        r, c, s, d, z = sharks[shark]
        if c == person:
            if min_r > r:
                min_r = r
                idx = shark
    if min_r < R+1:
        gotcha += sharks[idx][4]
        sharks.pop(idx)

    # 상어 이동
    for shark in range(len(sharks)):
        r, c, s, d, z = sharks[shark]
        sharks[shark] = moving(r, c, s, d, z)

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