N = int(input())
C = int(input())
array = [[0] * C for _ in range(N+1)]
is_visited = [0] * (N+1)

for i in range(C):
    X, Y = map(int, input().split())
    array[X][0] += 1
    array[X][array[X][0]] = Y
    array[Y][0] += 1
    array[Y][array[Y][0]] = X

queue = [0] * N * N
rear = -1
front = -1

queue[rear+1] = 1
rear += 1
is_visited[1] = 1

while front != rear:
    v = queue[front+1]
    front += 1
    for j in range(1, array[v][0]+1):
        if not is_visited[array[v][j]]:
            queue[rear+1] = array[v][j]
            rear += 1
            is_visited[array[v][j]] = 1

print(rear)
