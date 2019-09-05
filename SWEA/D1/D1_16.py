# 2068. 최대수 구하기
# 121ms, 145

T = int(input())

for i in range(T):
    num_list = list(map(int, input().split()))
    max_num = max(num_list)
    print(f'#{i + 1} {max_num}')
