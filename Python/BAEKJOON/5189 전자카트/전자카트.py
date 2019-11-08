import sys
sys.stdin = open('input.txt', 'r')


def min_road(s, total, c):
    global min_result
    if c == t-1:
        total += array[s][0]
        if min_result > total:
            min_result = total

    else:
        for e in range(1, t):
            if is_visited[e]:
                continue
            is_visited[e] = 1
            total += array[s][e]
            if total >= min_result:
                total -= array[s][e]
                is_visited[e] = 0
                continue
            min_road(e, total, c+1)
            total -= array[s][e]
            is_visited[e] = 0


T = int(input())
for i in range(1, T+1):
    t = int(input())
    array = [list(map(int, input().split())) for _ in range(t)]
    min_result = t * t * 101
    is_visited = [0] * t
    sn = 0
    total1 = 0
    count = 0
    min_road(sn, total1, count)
    print('#{} {}'.format(i, min_result))
