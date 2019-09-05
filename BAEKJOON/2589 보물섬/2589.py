X, Y = map(int, input().split())
array = [list(input()) for _ in range(X)]
max_length = 0

for x in range(X):
    for y in range(Y):
        is_visited = [[0] * Y for _ in range(X)]
        if array[x][y] == 'L' and not is_visited[x][y]:
            queue = [0] * X * Y
            rear = -1
            front = -1
            length = 0
            queue[rear + 1] = [x, y, length]
            rear += 1
            is_visited[x][y] = 1

            while rear != front:
                v1, v2, length = queue[front + 1]
                front += 1
                if length > max_length:
                    max_length = length
                dx = [-1, 0, 1, 0]
                dy = [0, 1, 0, -1]
                for d in range(4):
                    if 0 <= v1+dx[d] < X and 0 <= v2+dy[d] < Y:
                        if array[v1+dx[d]][v2+dy[d]] == 'L' and not is_visited[v1+dx[d]][v2+dy[d]]:
                            queue[rear + 1] = [v1 + dx[d], v2 + dy[d], length + 1]
                            rear += 1
                            is_visited[v1+dx[d]][v2+dy[d]] = 1

print(max_length)
