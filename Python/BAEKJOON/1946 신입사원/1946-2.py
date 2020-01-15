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

    # 초기값 설정
    ability, a, b = heappop(h)
    f1, f2, s1, s2 = a, b, a, b

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

    print(people + 1)
