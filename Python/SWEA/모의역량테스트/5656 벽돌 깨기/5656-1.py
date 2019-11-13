from collections import deque
from pprint import pprint
import sys
sys.stdin = open('input.txt')


def make_order(k, tmp):
    global orders
    if k == N:
        orders.append(tmp)
        return
    else:
        for i in range(W):
            make_order(k+1, tmp+[i])


def sorting():
    global copy_arr
    tmp_arr = [[[0] for _ in range(W)] for _ in range(H)]
    for w in range(W):
        tmp = []
        for h in range(H):
            if copy_arr[h][w]:
                tmp.append(copy_arr[h][w])
        tmp = [0] * (H-len(tmp)) + tmp
        for h in range(H-1, -1, -1):
            tmp_arr[h][w] = tmp[h]
    copy_arr = tmp_arr


def game(w):
    global copy_arr
    for h in range(H):
        if copy_arr[h][w]:
            q = deque([[h, w, copy_arr[h][w]]])
            while q:
                a, b, cnt = q.popleft()
                # print(a,b)
                # print(cnt)
                copy_arr[a][b] = 0
                for d in range(4):
                    aa, bb = a, b
                    for _ in range(cnt-1):
                        va, vb = aa+da[d], bb+db[d]
                        # print(va, vb)
                        if not (0 <= va < H and 0 <= vb < W): break
                        if copy_arr[va][vb]: q.append([va, vb, copy_arr[va][vb]])
                        copy_arr[va][vb] = 0
                        aa, bb = va, vb
            break


def counting():
    global remain_blocks
    for h in range(H):
        for w in range(W):
            if copy_arr[h][w]:
                remain_blocks += 1


da, db = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, int(input())+1):
    N, W, H = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    orders = []
    make_order(0, [])
    result = W * H
    for order in orders:
        copy_arr = [arr[h][:] for h in range(H)]
        remain_blocks = 0
        for o in order:
            game(o)
            sorting()
        counting()
        result = min(result, remain_blocks)
        if result == 0: break
        # print(order, result)
        # pprint(copy_arr)

    print('#{} {}'.format(tc, result))
    # break