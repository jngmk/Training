import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())

# 배열 만들기
size, n = 0, 0
while True:
    if 2 ** n >= N:
        size = 2 ** n
        break
    n += 1
arr = [0] * size * 2
for i in range(N):
    idx = size+i
    num = int(input())
    arr[idx] = num
    while True:
        if idx <= 1: break
        arr[idx//2] += num
        idx //= 2

# 명령 실행
for _ in range(M+L):
    c, n1, n2 = map(int, input().split())
    if c == 1:
        idx = size+n1-1
        v = n2 - arr[idx]
        while True:
            if idx == 0: break
            arr[idx] += v
            idx //= 2
    elif c == 2:
        s, e, total = size+n1-1, size+n2-1, 0
        while s <= e:
            # 시작하는 값이 홀수일 때
            if s % 2 == 1:
                total += arr[s]
                s += 1
            # 끝나는 값이 짝수일 때
            if e % 2 == 0:
                total += arr[e]
                e -= 1
            s //= 2
            e //= 2
        print(total)
