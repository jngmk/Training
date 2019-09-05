import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    N = int(input())
    money_list = []
    for j in range(N):
        p, m = map(float, input().split())
        money = p * m
        money_list.append(money)
    result = sum(money_list)
    print('#{0} {1:.6f}'.format(i+1, result))
