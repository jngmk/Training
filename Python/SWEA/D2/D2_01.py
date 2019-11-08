# 1204. 최빈수 구하기
# 170ms, 233
from collections import Counter

T = int(input())

for i in range(T):
    t = int(input())
    data_list = list(map(int, input().split()))

    cnt = Counter(data_list)
    mode = cnt.most_common()
    print(f'#{i + 1} {mode[0][0]}')


# https://codepractice.tistory.com/71