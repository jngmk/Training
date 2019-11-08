# 직사각형 네개의 합집합의 면적 구하기
# 29056KB, 56ms, 496B
input_list = []
for i in range(4):
    input_list += [input().split()]

xy_array = [[0] * 100 for _ in range(100)]
result = 0
for n in range(4):
    x1 = int(input_list[n][0])
    x2 = int(input_list[n][2])
    y1 = int(input_list[n][1])
    y2 = int(input_list[n][3])
    len_x = x2 - x1
    len_y = y2 - y1
    for x in range(x1, x1+len_x):
        for y in range(y1, y1+len_y):
            if xy_array[x][y] == 0:
                xy_array[x][y] += 1
                result += 1

print(result)
