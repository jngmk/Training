# 정올 정답, 백준 오답
N = int(input())
u, v, w, x, y = map(int, input().split())
array = [[0] * (N+2)]
array += [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
array += [[0] * (N+2)]
is_visited = [[0] * (N+2) for _ in range(N+2)]
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
result = []


def check_type(aa, bb):
    b_type = 0
    sa, sb = aa, bb
    while True:
        if array[aa][bb+db[1]] == 1:
            aa, bb = aa, bb+1
        else:
            d1 = bb
            break

    while True:
        if array[aa+da[2]][bb] == 1:
            aa, bb = aa+1, bb
        else:
            c1 = aa
            break

    while True:
        if array[sa+da[2]][sb] == 1:
            sa, sb = sa+1, sb
        else:
            c2 = sa
            break

    while True:
        if array[sa][sb+db[1]] == 1:
            sa, sb = sa, sb+1
        else:
            d2 = sb
            break

    if c1 != c2:
        if c2 > c1:
            b_type = 2
            ee = [c2, d1]
        else:
            b_type = 4
            ee = [c1, d1]
    elif d1 != d2:
        if d2 > d1:
            b_type = 3
            ee = [c1, d2]
        else:
            b_type = 1
            ee = [c1, d1]

    return b_type, ee


def match_block(b_shape, s, e):
    if b_shape == 1:
        if e[1] - s[1] + 1 != u:
            return 0
        for aa in range(s[0], e[0]+1):
            for bb in range(s[1], e[1]+1):
                if array[aa][bb] == 0:
                    sa, sb = aa, bb
                    break
        if sb - s[1] != w:
            return 0
        if sa + x != e[0]:
            return 0
        for aa in range(sa, sa+y):
            for bb in range(sb, sb+x):
                if array[aa][bb] == 1:
                    return 0
                else:
                    array[aa][bb] = 1


is_visited = [[0] * (N+2) for _ in range(N+2)]
for a in range(N):
    for b in range(N):
        if array[a][b] == 1 and not is_visited[a][b]:
            stack = []
            sa0, sb0 = a, b
            shape, end = check_type(a, b)
            ea0, eb0 = end
            stack.append((sa0, sb0))
            is_visited[sa0][sb0] = 1
            while stack:
                va, vb = stack.pop()
                for d in range(4):
                    ra = va+da[d]
                    rb = vb+db[d]
                    if 1 <= ra < N+1 and 1 <= rb < N+1:
                        if array[ra][rb] == 1 and not is_visited[ra][rb]:
                            stack.append((ra, rb))
                            is_visited[ra][rb] = 1
            temp = []
            if shape == 1:
                for a1 in range(sa0, ea0+1):
                    for b1 in range(sb0, eb0+1):
                        if array[a1][b1] == 0:
                            temp.append((a1, b1))
                if ea0+1+v > N+1:
                    check = 0
                else:
                    check = 1
                    for a1 in range(ea0+1, ea0+1+v):
                        for b1 in range(sb0, eb0+1):
                            if array[a1][b1] == 1:
                                check = 0
                                break

                    sa1, sb1 = temp[0]
                    ea1, eb1 = temp[-1]
                    if ea1 - sa1 + 1 != x:
                        check = 0
                    elif eb1 - sb1 + 1 != y:
                        check = 0
                    elif sb1 - sb0 != w:
                        check = 0
                    elif eb0 - sb0 + 1 != u:
                        check = 0

            elif shape == 2:
                for b1 in range(sb0, eb0 + 1):
                    for a1 in range(ea0, sa0-1, -1):
                        if array[a1][b1] == 0:
                            temp.append((a1, b1))
                if eb0+1+v > N+1:
                    check = 0
                else:
                    check = 1
                    for b1 in range(eb0+1, eb0+1+v):
                        for a1 in range(ea0, sa0-1, -1):
                            if array[a1][b1] == 1:
                                check = 0
                                break

                    sa1, sb1 = temp[0]
                    ea1, eb1 = temp[-1]
                    if sa1 - ea1 + 1 != y:
                        check = 0
                    elif eb1 - sb1 + 1 != x:
                        check = 0
                    elif ea0 - sa1 != w:
                        check = 0
                    elif ea0 - sa0 + 1 != u:
                        check = 0

            elif shape == 3:
                for a1 in range(ea0, sa0-1, -1):
                    for b1 in range(eb0, sb0-1, -1):
                        if array[a1][b1] == 0:
                            temp.append((a1, b1))

                if sa0-1-v < 1:
                    check = 0
                else:
                    check = 1
                    for a1 in range(sa0-1, sa0-1-v, -1):
                        for b1 in range(eb0, sb0-1, -1):
                            if array[a1][b1] == 1:
                                check = 0
                                break

                    sa1, sb1 = temp[0]
                    ea1, eb1 = temp[-1]
                    if sa1 - ea1 + 1 != x:
                        check = 0
                    elif sb1 - eb1 + 1 != y:
                        check = 0
                    elif eb0 - sb1 != w:
                        check = 0
                    elif eb0 - sb0 + 1 != u:
                        check = 0
            elif shape == 4:
                for b1 in range(eb0, sb0-1, -1):
                    for a1 in range(sa0, ea0+1):
                        if array[a1][b1] == 0:
                            temp.append((a1, b1))
                if sb0-1-v < 1:
                    check = 0
                else:
                    check = 1
                    for b1 in range(sb0-1, sb0-1-v, -1):
                        for a1 in range(sa0, ea0+1):
                            if array[a1][b1] == 1:
                                check = 0
                                break

                    sa1, sb1 = temp[0]
                    ea1, eb1 = temp[-1]
                    if ea1 - sa1 + 1 != y:
                        check = 0
                    elif sb1 - eb1 + 1 != x:
                        check = 0
                    elif sa1 - sa0 != w:
                        check = 0
                    elif ea0 - sa0 + 1 != u:
                        check = 0

            if check == 1:
                result.append(str(sa0)+' '+str(sb0))

print(len(result))
for res in result:
    print(res)
