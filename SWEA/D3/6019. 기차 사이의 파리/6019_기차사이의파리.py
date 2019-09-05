import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    D, A, B, F = map(int, input().split())
    result = (D /(A + B)) * F
    print('#{0} {1:.6f}'.format(i+1, result))
