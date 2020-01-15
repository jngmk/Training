import sys
from heapq import heappop, heappush
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    h = []
    passer = dict()
    people = 0
    for _ in range(N):
        a, b = map(int, input().split())
        heappush(h, (a+b, a, b))

    f1, f2, s1, s2 = N+1, N+1, N+1, N+1

    cnt = 0
    visited = [0, 0]
    find = False

    # 초기값 설정
    while True:
        cnt += 1
        ability, a, b = heappop(h)
        if (a, b) == (1, 1):
            find = True; break
        if a < f1:
            f1, f2 = a, b
            if visited[0]:
                s1, s2 = f1, f2
                f1, f2 = a, b
                visited[1] = 1
            else:
                visited[0] = 1
        else:
            s1, s2 = a, b
            visited[1] = 1

        if sum(visited) == 2: break

    if find: print(1); continue

    while h:
        ability, a, b = heappop(h)
        # 두 능력 다 안될 때
        if (a > f1 and b > f2) or (a > s1 and b > s2): continue

        if a < f1:
            if not passer.get((f1, f2)):
                people += 1
                passer[(f1, f2)] = 1
            f1, f2 = a, b
        if b < s2:
            if not passer.get((s1, s2)):
                people += 1
                passer[(s1, s2)] = 1
            s1, s2 = a, b

    print(people + 2)
