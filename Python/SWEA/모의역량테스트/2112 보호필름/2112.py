# itertools 로 투약횟수 작은 거부터 보는게 더 빠름,,
import sys
sys.stdin = open('input.txt')


def qualified(copy_arr):
    for w in range(W):
        flag = True
        now = copy_arr[0][w]
        cnt = 1
        for d in range(1, D):
            if copy_arr[d][w] != now:
                now = copy_arr[d][w]
                cnt = 0
            cnt += 1
            if cnt == K: flag = False; break
        if flag: return False
    return True


def comb(now, copy, c):
    global count
    if c >= count: return
    if qualified(copy):
        count = min(count, c)
        return
    for i in range(now, D):
        copy[i] = A[:]
        comb(i+1, copy, c+1)
        copy[i] = B[:]
        comb(i+1, copy, c+1)
        copy[i] = arr[i][:]


for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    A, B = [0] * W, [1] * W
    count = K
    comb(0, arr[:], 0)
    print('#{} {}'.format(tc, count))
