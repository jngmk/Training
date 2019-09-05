# 1959. 두 개의 숫자열
# 122ms, 712

T = int(input())
for i in range(T):
    a_len, b_len = map(int, input().split(' '))
    a_list = list(map(int, input().split(' ')))
    b_list = list(map(int, input().split(' ')))
    para_num = abs(a_len - b_len) + 1
    result = 0

    if a_len >= b_len:
        for j in range(para_num):
            total = 0
            for k in range(b_len):
                total += a_list[k + j] * b_list[k]
            if result < total:
                result = total
    else:
        for j in range(para_num):
            total = 0
            for k in range(a_len):
                total += a_list[k] * b_list[k + j]
            if result < total:
                result = total
    
    print(f'#{i + 1} {result}')
