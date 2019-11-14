from collections import deque
import sys
sys.stdin = open('input.txt')


def rotation(ii, dd):
    global t, visited
    visited[ii] = 1
    if ii + 1 < 4 and not visited[ii+1]:
        if t[ii][2] != t[ii+1][6]:
            rotation(ii+1, dd*(-1))
    if ii - 1 >= 0 and not visited[ii-1]:
        if t[ii][6] != t[ii-1][2]:
            rotation(ii-1, dd*(-1))
    if dd == 1:
        t[ii].rotate(1)
    else:
        t[ii].rotate(-1)


for tc in range(1, int(input())+1):
    K = int(input())
    t = [deque(), deque(), deque(), deque()]
    for i in range(4):
        t[i].extend(list(map(int, input().split())))
    for _ in range(K):
        idx, d = map(int, input().split())
        visited = [0, 0, 0, 0]
        rotation(idx-1, d)
    result = 0
    for i in range(4):
        if t[i][0] == 1:
            result += 2 ** i
    print('#{} {}'.format(tc, result))
