import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    s1, s2 = map(int, input().split())
    cu = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    e1, e2 = map(int, input().split())

    q = deque([(s1, s2)])
    is_arrived = False
    while q:
        p1, p2 = q.popleft()
        if abs(e1-p1) + abs(e2-p2) <= 1000:
            is_arrived = True; break
        for c in range(N):
            if visited[c]: continue
            c1, c2 = cu[c]
            if abs(c1-p1) + abs(c2-p2) > 1000: continue
            visited[c] = 1
            q.append((c1, c2))

    print('happy' if is_arrived else 'sad')
