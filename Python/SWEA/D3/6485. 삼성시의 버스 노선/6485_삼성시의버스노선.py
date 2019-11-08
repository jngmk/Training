import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    N = int(input())
    stop_list = []

    for j in range(N):
        A, B = map(int, input().split())
        stop_list.append(list(range(A, B+1)))

    P = int(input())
    stop_by_list = [[0, 0] for _ in range(P)]

    for p in range(P):
        stop_by_list[p][0] = int(input())
        for j in stop_list:
            if stop_by_list[p][0] in j:
                stop_by_list[p][1] += 1

    result = ''
    for r in range(len(stop_by_list)):
        result += str(stop_by_list[r][1]) + ' '

    print('#{0} {1}'.format(i+1, result))
