from collections import deque
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    operators = list(map(int, input().split()))  # '+', '-', '*', '//'
    num_arr = list(map(int, input().split()))
    max_num = -1000000000
    min_num = 1000000000
    q = deque([[num_arr[0], 1, operators]])
    while q:
        num, k, operators = q.popleft()
        if k == N:
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            continue
        for i in range(4):
            if operators[i] == 0: continue
            if i == 0:
                tmp_num = num + num_arr[k]
            elif i == 1:
                tmp_num = num - num_arr[k]
            elif i == 2:
                tmp_num = num * num_arr[k]
            else:
                if num * num_arr[k] < 0:
                    tmp_num = ((num * (-1)) // num_arr[k]) * (-1)
                else:
                    tmp_num = num // num_arr[k]
            operators[i] -= 1
            q.append([tmp_num, k+1, operators[:]])
            operators[i] += 1

    print('#{} {}'.format(tc, max_num-min_num))
