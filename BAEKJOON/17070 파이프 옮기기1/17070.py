N = int(input())
array = [list(map(int, input().split()))for _ in range(N)]
# print(array)
pipe = 'a'
now1, now2 = (0, 1)
cnt = 0


def connect(p, n1, n2):
    global cnt
    if (n1, n2) == (N-1, N-1):
        cnt += 1
        return
    if p == 'a':
        if not array[n1][n2 + 1] and n2+1 < N:
            connect('a', n1, n2 + 1)
        if not array[n1][n2+1] and not array[n1+1][n2] and not array[n1+1][n2+1] and n1+1 < N and n2+1 < N:
            connect('c', n1 + 1, n2 + 1)
    if p == 'b':
        if not array[n1 + 1][n2] and n1+1 < N:
            connect('b', n1 + 1, n2)
        if not array[n1][n2+1] and not array[n1+1][n2] and not array[n1+1][n2+1] and n1+1 < N and n2+1 < N:
            connect('c', n1 + 1, n2 + 1)
    if p == 'c':
        if not array[n1][n2+1] and n2+1 < N:
            connect('a', n1, n2 + 1)
        if not array[n1 + 1][n2] and n1+1 < N:
            connect('b', n1 + 1, n2)
        if not array[n1][n2+1] and not array[n1+1][n2] and not array[n1+1][n2+1] and n1+1 < N and n2+1 < N:
            connect('c', n1 + 1, n2 + 1)


connect(pipe, now1, now2)
print(cnt)