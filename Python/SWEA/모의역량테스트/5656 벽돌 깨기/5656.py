from collections import deque
from pprint import pprint
import sys
sys.stdin = open('input.txt')


def sorting(copy, visited):
    tmp_arr = [[[0] for _ in range(W)] for _ in range(H)]
    # print(visited)
    for w in range(W):
        tmp = []
        for h in range(H):
            if copy[h][w]:
                if [h, w] in visited: continue
                tmp.append(copy[h][w])
        tmp = [0] * (H-len(tmp)) + tmp
        # print(tmp)
        for h in range(H-1, -1, -1):
            tmp_arr[h][w] = tmp[h]
    # print('sort')
    # pprint(tmp_arr)
    return tmp_arr


def game(copy_arr, k, broken, visited):
    print(k, visited)
    pprint(copy_arr)
    # print(broken)
    global max_broken
    if k == N:
        if broken <= max_broken: return
        max_broken = max(max_broken, broken)
        # pprint(copy_arr)
        return
    else:
        for w in range(W):
            for h in range(H):
                tmp_visited = visited[:]
                tmp_broken = broken
                if copy_arr[h][w] and [h, w] not in tmp_visited:
                    q = deque()
                    q.append([h, w])
                    tmp_visited.append([h, w])
                    print(h, w)
                    while q:
                        a, b = q.popleft()
                        # print(a, b)
                        tmp_broken += 1
                        for d in range(4):
                            n = 1
                            count = copy_arr[a][b]
                            aa, bb = a, b
                            while True:
                                if n >= count: break
                                va, vb = aa+da[d], bb+db[d]
                                # print(n, va, vb)
                                if not (0 <= va < H and 0 <= vb < W): break
                                if not copy_arr[va][vb]: n += 1; continue
                                if [va, vb] not in tmp_visited:
                                    q.append([va, vb])
                                    tmp_visited.append([va, vb])
                                aa, bb = va, vb
                                n += 1
                    game(sorting(copy_arr, tmp_visited), k+1, tmp_broken, [])
                    break


da, db = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, int(input())+1):
    N, W, H = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    total = 0
    for ww in range(W):
        for hh in range(H):
            if arr[ww][hh]:
                total += 1
    max_broken = 0
    game(arr[:], 0, 0, [])
    print('#{} {}'.format(tc, total - max_broken))
    break