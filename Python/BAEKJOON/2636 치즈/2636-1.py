from collections import deque
from pprint import pprint


def air():
    global arr
    q = deque([[0, 0]])
    arr[0][0] = 2
    while q:
        a, b = q.popleft()
        for da, db in di:
            va, vb = a+da, b+db
            if not (0 <= va < A and 0 <= vb < B): continue
            if not arr[va][vb]:
                q.append([va, vb])
                arr[va][vb] = 2


di = [(-1, 0), (1, 0), (0, 1), (0, -1)]
A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(A)]
cnt = 1
while True:
    air()

    for a in range(A):
        for b in range(B):
            if arr[a][b] == 1:
                if arr[a-1][b] == 2 or arr[a+1][b] == 2 or arr[a][b-1] == 2 or arr[a][b+1] == 2:
                    arr[a][b] = 3
                else:
                    arr[a][b] = 4

    cheese = 0
    for a in range(A):
        for b in range(B):
            if arr[a][b] == 2: arr[a][b] = 0
            elif arr[a][b] == 3: cheese += 1; arr[a][b] = 0
            elif arr[a][b] == 4: arr[a][b] = 1

    if not sum(sum(arr, [])):
        print(cnt)
        print(cheese)
        break

    cnt += 1
