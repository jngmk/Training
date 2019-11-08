# 2063. 중간값 찾기
# 120ms, 154

n = int(input())
num_list = list(map(int, input().split()))
sorted_num_list = sorted(num_list)
median_index = n // 2

print(sorted_num_list[median_index])
