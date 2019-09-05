N = int(input())
array = [[0] * N for _ in range(N+1)]

while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    array[a][0] += 1
    array[a][array[a][0]] = b
    array[b][0] += 1
    array[b][array[b][0]] = a

queue = [0] * N * N
rear = -1
front = -1
results = []
min_num = N

for n in range(1, N+1):
    length = 0
    queue[rear+1] = n, length
    rear += 1
    is_visited = [0] * (N + 1)
    is_visited[n] = 1

    while front != rear:
        v, length = queue[front+1]
        front += 1
        for i in range(1, array[v][0]+1):
            if not is_visited[array[v][i]]:
                queue[rear+1] = array[v][i], length + 1
                rear += 1
                is_visited[array[v][i]] = 1

    if length < min_num:
        min_num = length
        results = [n]
    elif length == min_num:
        results.append(n)

print(min_num, end=' ')
print(len(results))
for result in sorted(results):
    print(result, end=' ')
