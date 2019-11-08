import sys
sys.stdin = open('input.txt', 'r')


def max_total(n, total):
    global min_result
    if n == t:
        if total < min_result:
            min_result = total
    else:
        for j in range(t):
            if is_visited[j]:
                continue
            total += array[n][j]
            is_visited[j] = 1
            if min_result < total:
                is_visited[j] = 0
                total -= array[n][j]
                continue
            max_total(n+1, total)
            is_visited[j] = 0
            total -= array[n][j]


T = int(input())
for i in range(1, T+1):
    t = int(input())
    array = [list(map(int, input().split())) for _ in range(t)]
    n1 = 0
    total1 = 0
    min_result = 10 * t
    is_visited = [0] * (t + 1)
    max_total(n1, total1)
    print('#{0} {1}'.format(i, min_result))
