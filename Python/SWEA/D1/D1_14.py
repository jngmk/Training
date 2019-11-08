# 2058. 자릿수 더하기
# 122ms, 84

num_list = str(input())
sum = 0
for num in num_list:
    sum += int(num)
print(sum)
