import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    num_list = list(map(int, input().split()))
    result_set = set()
    for a in range(5):
        for b in range(a+1, 6):
            for c in range(b+1, 7):
                num = num_list[a] + num_list[b] + num_list[c]
                result_set.add(num)

    result = sorted(result_set)[-5]
    print('#{0} {1}'.format(i+1, result))
