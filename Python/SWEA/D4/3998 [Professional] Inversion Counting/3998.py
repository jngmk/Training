# import sys
# sys.stdin = open('input.txt')
from heapq import heappush, heappop


def inversion_counting():
    global cnt
    ss, ee = s, e
    while ss < ee:
        if ss % 2 == 1:
            cnt += arr[ss]
            ss += 1
        if ee % 2 == 0:
            cnt += arr[ee]
            ee -= 1
        ss >>= 1
        ee >>= 1
    if ss == ee:
        cnt += arr[ss]


for tc in range(1, int(input())+1):
    N = int(input())
    tmp = list(map(int, input().split()))
    cnt = 0

    # make indexed tree
    n = 0
    while True:
        if N < (1 << n): break
        n += 1
    arr = [0] * (1 << (n+1))

    # inversion counting
    h = []
    for i in range(N):
        heappush(h, [-tmp[i], -i])
    s = 1 << n
    for _ in range(N):
        v, i = heappop(h)
        e = s - i
        inversion_counting()

        # 구간합 갱신
        arr[e] = 1
        while True:
            if e <= 1: break
            arr[e >> 1] += 1
            e >>= 1

    print('#{} {}'.format(tc, cnt))
