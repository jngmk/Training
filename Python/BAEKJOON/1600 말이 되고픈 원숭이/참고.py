from collections import deque

k = int(input())
w, h = map(int, input().split())
graph = []
for i in range(h):
    graph.append(list(map(int, input().split())))
visit = [[(k+1) for i in range(w)]for j in range(h)]

visit[0][0] = 0
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
horsedir = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
queue = deque([[0, 0, 0, 0]])
fn = 0
while queue:
    temp = queue.popleft()
    for nextdir in dir:
        nextx = nextdir[0] + temp[0]
        nexty = nextdir[1] + temp[1]
        if -1 < nextx < h and -1 < nexty < w and graph[nextx][nexty] == 0 and visit[nextx][nexty] > temp[2]:
            visit[nextx][nexty] = temp[2]
            queue.append([nextx, nexty, temp[2], temp[3] + 1])

    temp[2] += 1
    for nextdir in horsedir:
        nextx = nextdir[0] + temp[0]
        nexty = nextdir[1] + temp[1]
        if -1 < nextx < h and -1 < nexty < w and graph[nextx][nexty] == 0 and visit[nextx][nexty] > temp[2]:
            visit[nextx][nexty] = temp[2]
            queue.append([nextx, nexty, temp[2], temp[3] + 1])

    if visit[h-1][w-1] != (k+1):
        fn = 1
        print(temp[3] + 1)
        break
if fn == 0:
    print(-1)