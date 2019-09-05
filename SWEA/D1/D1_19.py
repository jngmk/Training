# 2072.
# 116ms, 215

n = int(input())
for i in range(n):
    sum = 0
    num = list(map(int,input().split()))
    for j in range(10):
        if num[j] % 2 == 1:
            sum = sum + num[j]
    
    print('#{0} {1}'.format(i+1, sum))



