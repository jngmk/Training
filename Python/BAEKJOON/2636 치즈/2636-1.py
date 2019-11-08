# 미결
X, Y = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(X)]
is_visited = [[0] * X for _ in range(Y)]
stack = [0] * X * Y
top = -1
check = 1

for a in range(X):
    for b in range(Y):
        if array[a][b] == 0:
            stack[top+1] = (a, b)
            top += 1
            array[a][b] = 2
            is_visited[a][b] = check
            while top != -1:
                v1, v2 = stack[top]
                top -= 1
                dx = [-1, 0, 1, 0]
                dy = [0, 1, 0, -1]
                for d in range(4):
                    if 0 <= v1+dx[d] < X and 0 <= v2+dy[d] < Y:
                        if array[v1+dx[d]][v2+dy[d]] == 0:
                            stack[top+1] = (v1+dx[d], v2+dy[d])
                            top += 1
                            array[v1 + dx[d]][v2 + dy[d]] = 2
                            is_visited[v1 + dx[d]][v2 + dy[d]] = check
            break
        break


for x in range(X):
    for y in range(Y):
        if array[x][y] == 2 and is_visited == check:
            stack[top + 1] = (x, y)
            top += 1
            is_visited[x][y] = check + 1
            while top != -1:
                v1, v2 = stack[top]
                top -= 1
                dx = [-1, 0, 1, 0]
                dy = [0, 1, 0, -1]
                for d in range(4):
                    if 0 <= v1+dx[d] < X and 0 <= v2+dy[d] < Y:
                        if array[v1+dx[d]][v2+dy[d]] == 2:
                            stack[top+1] = (v1+dx[d], v2+dy[d])
                            top += 1
                            is_visited[v1+dx[d]][v2+dy[d]] = check + 1
                        elif array[v1+dx[d]][v2+dy[d]] == 1:
                            array[v1+dx[d]][v2+dy[d]] = 2
                            is_visited[v1+dx[d]][v2+dy[d]] = check + 2
                        elif array[v1 + dx[d]][v2 + dy[d]] == 0:
                            stack[top+1] = (v1+dx[d], v2+dy[d])
                            top += 1
                            array[v1 + dx[d]][v2 + dy[d]] = 2
                            is_visited[v1 + dx[d]][v2 + dy[d]] = check
            break
        break

print(array)
