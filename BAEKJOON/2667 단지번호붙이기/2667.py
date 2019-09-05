T = int(input())
array = [list(input()) for _ in range(T)]
result_list = []


def is_house(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = [0] * T * T
    top = -1
    count = 0

    stack[top+1] = (x, y)
    array[x][y] = '0'
    top += 1
    while top != -1:
        v1, v2 = stack[top]
        top -= 1
        count += 1
        for i in range(4):
            if T > v1 + dx[i] >= 0 and T > v2 + dy[i] >= 0:
                if int(array[v1 + dx[i]][v2 + dy[i]]):
                    stack[top + 1] = (v1 + dx[i], v2 + dy[i])
                    array[v1 + dx[i]][v2 + dy[i]] = '0'
                    top += 1

    return count


for x1 in range(T):
    for y1 in range(T):
        if array[x1][y1] == '1':
            start_x, start_y = x1, y1
            result_list += [is_house(start_x, start_y)]


result_list = sorted(result_list)
print(len(result_list))
for num in result_list:
    print(num)
