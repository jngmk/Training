from collections import deque


def calc(a, o, b):
    if o == '-':
        return a-b
    if o == '+':
        return a+b
    if o == '*':
        return a*b


N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
max_nums = -float('inf')
min_nums = float('inf')
for y in range(N):
    for x in range(N):
        if arr[y][x] not in ['-', '+', '*']:
            arr[y][x] = int(arr[y][x])

q = deque([[0, 0, [arr[0][0]]]])
while q:
    y, x, num_list = q.popleft()
    if len(num_list) == 3:
        num_list = [calc(num_list[0], num_list[1], num_list[2])]
    if (y, x) == (N-1, N-1):
        max_nums = max(max_nums, num_list[0])
        min_nums = min(min_nums, num_list[0])
    for dy, dx in (0, 1), (1, 0):
        ny, nx = y+dy, x+dx
        if not (ny < N and nx < N): continue
        q.append([ny, nx, num_list+[arr[ny][nx]]])

print(max_nums, min_nums)
