N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
test_array = array
is_test = [0] * 101
max_num = 0


def is_safe_zone(h):
    if not is_test[h]:
        is_test[h] = 1
        num1 = []
        stack = [0] * N * N
        top = -1
        is_visited = [[0] * N for _ in range(N)]
        for x1 in range(N):
            for y1 in range(N):
                count = 0
                if array[x1][y1] - h > 0 and not is_visited[x1][y1]:
                    stack[top + 1] = x1, y1
                    is_visited[x1][y1] = 1
                    top += 1
                    num1.append(count)
                    while top != -1:
                        v1, v2 = stack[top]
                        top -= 1
                        dx = [-1, 0, 1, 0]
                        dy = [0, 1, 0, -1]
                        for d in range(4):
                            if 0 <= v1 + dx[d] < N and 0 <= v2 + dy[d] < N:
                                if array[v1 + dx[d]][v2 + dy[d]] - h > 0 and not is_visited[v1 + dx[d]][v2 + dy[d]]:
                                    stack[top + 1] = (v1 + dx[d], v2 + dy[d])
                                    top += 1
                                    is_visited[v1 + dx[d]][v2 + dy[d]] = 1
        return len(num1)
    else:
        return 0


for x in range(N):
    for y in range(N):
        h1 = array[x][y]
        num = is_safe_zone(h1)
        if max_num < num:
            max_num = num
        num = is_safe_zone(h1-1)
        if max_num < num:
            max_num = num

print(max_num)
