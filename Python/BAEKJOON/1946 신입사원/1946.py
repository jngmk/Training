import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    a, b = map(int, input().split())
    f1, f2, s1, s2 = a, b, a, b  # 1차 우수자, 2차 우수자
    people = 0
    for _ in range(N-1):
        a, b = map(int, input().split())
        # 두 능력 다 안될 때
        if (a > f1 and b > f2) or (a > s1, b > s2): continue
        # 1차 우수자보다 성적이 좋을 때
        if a < f1:
            people += 1
            f1, f2 = a, b
        # 1차는 떨어질 때 2차 우수자와 비교
        elif b < s2:

        pass