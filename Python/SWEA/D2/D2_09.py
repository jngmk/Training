# 1948. 날짜 계산기
# 170ms, 209

from datetime import date

T = int(input())
for i in range(T):
    m1, d1, m2, d2 = map(int, input().split(' '))
    result = (date(2019, m2, d2) - date(2019, m1, d1)).days
    print(f'#{i + 1} {result + 1}')
