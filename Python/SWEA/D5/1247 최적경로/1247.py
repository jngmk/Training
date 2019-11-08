import sys
sys.stdin = open('input.txt', 'r')


def distance(n1, n2):
    x1, y1 = places[n1][0], places[n1][1]
    x2, y2 = places[n2][0], places[n2][1]
    dx = x1 - x2; dy = y1 - y2

    return abs(dx) + abs(dy)


def drop_by(s, cnt, tot):
    global min_dis
    if cnt == N+1:
        tot += distance(s, 2)
        if min_dis > tot:
            min_dis = tot
        tot -= distance(s, 2)
    else:
        for i in range(3, N+3):
            if is_visited[i]:
                continue
            is_visited[i] = 1
            tot += distance(s, i)
            if min_dis < tot:
                is_visited[i] = 0
                tot -= distance(s, i)
                continue
            drop_by(i, cnt+1, tot)
            is_visited[i] = 0
            tot -= distance(s, i)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    temp_list = list(map(int, input().split()))
    places = [[-1, -1]]
    for n in range(N+2):
        a = temp_list[2*n]
        b = temp_list[2*n+1]
        places.append([a, b])
    sx = 1
    count = 1
    min_dis = 2000
    total = 0
    is_visited = [0] * (N+3)
    drop_by(sx, count, total)

    print('#{} {}'.format(t, min_dis))
