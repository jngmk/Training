from pprint import pprint
import sys
sys.stdin = open('input.txt')

di = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
for tc in range(1, int(input())+1):
    M, C = map(int, input().split())
    move_a = [0]+list(map(int, input().split()))
    move_b = [0]+list(map(int, input().split()))
    arr = [[[] for _ in range(11)] for _ in range(11)]
    P = [0] * (C+1)
    for idx in range(1, C+1):
        b, a, t, p = map(int, input().split())
        for r in range(a-t, a+t+1):
            tt = t - abs(a-r)
            for c in range(b-tt, b+tt+1):
                if not (1 <= r < 11 and 1 <= c < 11): continue
                if abs(r-a) + abs(c-b) <= t:
                    arr[r][c].append(idx)
        P[idx] = p

    charging_amount = 0
    a, b, c, d = 1, 1, 10, 10
    for i in range(M+1):
        da, db = di[move_a[i]]; dc, dd = di[move_b[i]]
        va, vb, vc, vd = a+da, b+db, c+dc, d+dd
        bc1, bc2 = arr[va][vb], arr[vc][vd]
        tmp = 0
        if bc1 and bc2:
            for idx1 in bc1:
                for idx2 in bc2:
                    if idx1 == idx2:
                        tmp = max(tmp, P[idx1])
                    else:
                        tmp = max(tmp, P[idx1]+P[idx2])
        elif bc1 and not bc2:
            for idx1 in bc1:
                tmp = max(tmp, P[idx1])
        elif not bc1 and bc2:
            for idx2 in bc2:
                tmp = max(tmp, P[idx2])
        charging_amount += tmp
        a, b, c, d = va, vb, vc, vd

    print('#{} {}'.format(tc, charging_amount))
    # break