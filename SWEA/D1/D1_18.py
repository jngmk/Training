# 2071. 평균값 구하기
# 119ms, 237

T = int(input())

for i in range(T):
    num_list = list(map(int, input().split()))
    total_num = sum(num_list)
    average_num = total_num / len(num_list)
    average_num = round(average_num)
    
    print(f'#{i + 1} {average_num}')
