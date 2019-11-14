from collections import deque
import sys
sys.stdin = open('input.txt')


def game(k, copy_arr):
    global remain_blocks
    blocks = 0
    for h in range(H):
        for w in range(W):
            if copy_arr[h][w]:
                blocks += 1
    remain_blocks = min(remain_blocks, blocks)
    if not remain_blocks: return
    if k == N:
        return
    else:
        for w in range(W):
            for h in range(H):
                next_arr = [copy_arr[i][:] for i in range(H)]
                # 블록 부수기
                if next_arr[h][w]:
                    broken = 0
                    q = deque([[h, w, next_arr[h][w]]])
                    next_arr[h][w] = 0
                    while q:
                        a, b, cnt = q.popleft()
                        broken += 1
                        for da, db in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            va, vb = a, b
                            for _ in range(cnt - 1):
                                va, vb = va + da, vb + db
                                if not (0 <= va < H and 0 <= vb < W): break
                                if next_arr[va][vb] == 0: continue
                                q.append([va, vb, next_arr[va][vb]])
                                next_arr[va][vb] = 0
                    # 블록 재정렬
                    if broken != 1:
                        for ww in range(W):
                            tmp = [0] * H
                            t = H-1
                            for hh in range(H-1, -1, -1):
                                if next_arr[hh][ww]:
                                    tmp[t] = next_arr[hh][ww]
                                    t -= 1
                            for hh in range(H-1, -1, -1):
                                next_arr[hh][ww] = tmp[hh]
                    game(k+1, next_arr)
                    break


for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    remain_blocks = W * H
    game(0, arr)
    print('#{} {}'.format(tc, remain_blocks))
