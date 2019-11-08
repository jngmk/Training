# 1288. 새로운 불면증 치료법
# 161ms, 362
def add_num(num, c_list):
    for i in str(num):
        if i not in c_list:
            c_list.append(i)
    return c_list


T = int(input())
for i in range(T):
    count_sheep = int(input())
    j = 1
    count_list = []
    while len(count_list) < 10:
        add_num(j * count_sheep, count_list)
        j += 1
    print(f'#{i + 1} {count_sheep * (j - 1)}')
