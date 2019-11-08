# 2019.
# 127ms, 142

n = int(input())
sum = 1
for i in range(0, n+1):
    if i == 0:
        sum = sum * 1
    else:
        sum = sum * 2
    print(sum, end=' ')
