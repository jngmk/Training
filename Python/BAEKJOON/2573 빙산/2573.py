N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
count = -1
result = 0
stack = [0] * N * M
top = -1


while True:
    if count >= 2:
        break
    elif count == 0:
        result = 1
        break

    is_visited = [[0] * M for _ in range(N)]
    count = 0
    result += 1
    for x in range(N):
        for y in range(M):
            if array[x][y] > 0 and not is_visited[x][y]:
                stack[top+1] = (x, y)
                top += 1
                count += 1
                while top != -1:
                    v1, v2 = stack[top]
                    top -= 1
                    is_visited[v1][v2] = 1

                    dx = [-1, 0, 1, 0]
                    dy = [0, 1, 0, -1]
                    for d in range(4):
                        if 0 <= v1+dx[d] < N and 0 <= v2+dy[d] < M:
                            if array[v1+dx[d]][v2+dy[d]] > 0 and not is_visited[v1+dx[d]][v2+dy[d]]:
                                stack[top+1] = (v1+dx[d], v2+dy[d])
                                top += 1
                                is_visited[v1+dx[d]][v2+dy[d]] = 1
                            elif array[v1+dx[d]][v2+dy[d]] == 0 and not is_visited[v1+dx[d]][v2+dy[d]]:
                                array[v1][v2] -= 1
                                if array[v1][v2] < 0:
                                    array[v1][v2] = 0

print(result-1)
