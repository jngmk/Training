import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
board = [list(map(int, input().strip().split())) for _ in range(N)]
trip = list(map(int, input().strip().split()))
q = [trip[0]-1]
trip = set(trip)
visited = [0] * M
visited[q[0]] = 1
find = False

while q:
    v = q.pop(0)
    for t in trip:
        if not visited[t-1]: break
    else:
        find = True

    if find: break

    for i in range(N):
        if board[v][i] == 1:
            if visited[i]: continue
            q.append(i)
            visited[i] = 1

print('YES' if find else 'NO')
