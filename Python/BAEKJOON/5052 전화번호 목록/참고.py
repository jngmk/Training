import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    a = sorted(input().strip() for i in range(n))
    r = 1
    for i in range(1, n):
        if a[i-1] == a[i][:len(a[i-1])]:
            print("NO")
            break
    else:
        print("YES")
