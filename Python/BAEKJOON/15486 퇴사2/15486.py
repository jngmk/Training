# 시간 초과
from heapq import heappop, heappush

N = int(input())
arr = [None] * N
result = 0
for i in range(N):
    t, p = map(int, input().split())
    arr[i] = [p, i+t]

pay_list = []
for i in range(N):
    if arr[i][1] > N: continue
    max_pay = 0
    tmp = pay_list[:]
    for j in range(i):
        pay, t = heappop(tmp)
        if t <= i:
            max_pay = -pay
            break
    heappush(pay_list, [-(arr[i][0]+max_pay), arr[i][1]])
    result = max(result, arr[i][0]+max_pay)
print(result)
