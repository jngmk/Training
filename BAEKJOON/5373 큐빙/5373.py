def align(x):
    if x == 'U':
        rotate(U, B, 2, L, 0, R, 0, F, 0)
    elif x == 'F':
        rotate(F, U, 2, L, 1, R, 3, D, 0)
    elif x == 'D':
        rotate(D, F, 2, L, 2, R, 2, B, 0)
    elif x == 'B':
        rotate(B, D, 2, L, 3, R, 1, U, 0)
    elif x == 'L':
        rotate(L, U, 3, B, 3, F, 3, D, 3)
    elif x == 'R':
        rotate(R, U, 1, F, 1, B, 1, D, 1)


def rotate(a, b, n1, c, n2, d, n3, e, n4):
    global U, F, D, B, L, R
    if r == '+':
        # 정면 돌리기
        temp = []
        for t2 in range(3):
            for t1 in range(2, -1, -1):
                temp.append(a[t1][t2])
        t = 0
        for t1 in range(3):
            for t2 in range(3):
                a[t1][t2] = temp[t]
                t += 1

        # 측면 돌리기
        bn = change[n1]
        b1 = b[bn[0][0]][bn[0][1]]
        b2 = b[bn[1][0]][bn[1][1]]
        b3 = b[bn[2][0]][bn[2][1]]

        cn = change[n2]
        c1 = c[cn[0][0]][cn[0][1]]
        c2 = c[cn[1][0]][cn[1][1]]
        c3 = c[cn[2][0]][cn[2][1]]

        dn = change[n3]
        d1 = d[dn[0][0]][dn[0][1]]
        d2 = d[dn[1][0]][dn[1][1]]
        d3 = d[dn[2][0]][dn[2][1]]

        en = change[n4]
        e1 = e[en[0][0]][en[0][1]]
        e2 = e[en[1][0]][en[1][1]]
        e3 = e[en[2][0]][en[2][1]]

        b[bn[0][0]][bn[0][1]], b[bn[1][0]][bn[1][1]], b[bn[2][0]][bn[2][1]] = c1, c2, c3
        c[cn[0][0]][cn[0][1]], c[cn[1][0]][cn[1][1]], c[cn[2][0]][cn[2][1]] = e1, e2, e3
        d[dn[0][0]][dn[0][1]], d[dn[1][0]][dn[1][1]], d[dn[2][0]][dn[2][1]] = b1, b2, b3
        e[en[0][0]][en[0][1]], e[en[1][0]][en[1][1]], e[en[2][0]][en[2][1]] = d1, d2, d3

    else:
        # 정면 돌리기
        temp = []
        for t2 in range(2, -1, -1):
            for t1 in range(3):
                temp.append(a[t1][t2])
        t = 0
        for t1 in range(3):
            for t2 in range(3):
                a[t1][t2] = temp[t]
                t += 1

        # 측면 돌리기
        bn = change[n1]
        b1 = b[bn[0][0]][bn[0][1]]
        b2 = b[bn[1][0]][bn[1][1]]
        b3 = b[bn[2][0]][bn[2][1]]

        cn = change[n2]
        c1 = c[cn[0][0]][cn[0][1]]
        c2 = c[cn[1][0]][cn[1][1]]
        c3 = c[cn[2][0]][cn[2][1]]

        dn = change[n3]
        d1 = d[dn[0][0]][dn[0][1]]
        d2 = d[dn[1][0]][dn[1][1]]
        d3 = d[dn[2][0]][dn[2][1]]

        en = change[n4]
        e1 = e[en[0][0]][en[0][1]]
        e2 = e[en[1][0]][en[1][1]]
        e3 = e[en[2][0]][en[2][1]]

        b[bn[0][0]][bn[0][1]], b[bn[1][0]][bn[1][1]], b[bn[2][0]][bn[2][1]] = d1, d2, d3
        c[cn[0][0]][cn[0][1]], c[cn[1][0]][cn[1][1]], c[cn[2][0]][cn[2][1]] = b1, b2, b3
        d[dn[0][0]][dn[0][1]], d[dn[1][0]][dn[1][1]], d[dn[2][0]][dn[2][1]] = e1, e2, e3
        e[en[0][0]][en[0][1]], e[en[1][0]][en[1][1]], e[en[2][0]][en[2][1]] = c1, c2, c3


change = {0: [(0, 2), (0, 1), (0, 0)],
          1: [(2, 2), (1, 2), (0, 2)],
          2: [(2, 0), (2, 1), (2, 2)],
          3: [(0, 0), (1, 0), (2, 0)]}

for _ in range(int(input())):
    N = int(input())
    rotations = list(map(str, input().split()))
    U = [['w'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]
    for item in rotations:
        i, r = item[0], item[1]
        align(i)

    for i in range(3):
        tmp = ''
        for j in range(3):
            tmp += U[i][j]
        print(tmp)
