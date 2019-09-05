import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    N = int(input())
    input_list = list(map(int, input().split()))
    result_list = []

    result = -1
    for j in range(N - 1):
        for k in range(j + 1, N):
            num = str(input_list[j] * input_list[k])
            for m in range(len(num)-1):
                if int(num[m]) > int(num[m+1]):
                    break
            else:
                result = max(result, int(num))

    print('#{0} {1}'.format(i+1, result))
