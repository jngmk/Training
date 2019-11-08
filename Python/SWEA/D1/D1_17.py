# 2070. 큰 놈, 작은 놈, 같은 놈
# 123ms, 219

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '='
    
    print(f'#{i + 1} {result}')
