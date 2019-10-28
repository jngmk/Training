def region1():
    tmp1 = 0
    cnt = -1
    for x in range(a+d1, -1, -1):
        cnt += 1
        for y in range(b-d1+cnt, -1, -1):
            if a > x and y > b:
                continue
            tmp1 += arr[x][y]
    return tmp1


def region2():
    tmp1 = 0
    cnt = -1
    for y in range(b+1, N):
        cnt += 1
        for x in range(a+cnt, -1, -1):
            if b < y and x > a:
                continue
            tmp1 += arr[x][y]
    return tmp1


def region3():
    tmp1 = 0
    cnt = -1
    for y in range(b-d1+d2-1, -1, -1):
        cnt += 1
        for x in range(a+d1+d2-cnt, N):
            if b-d1 > y and x < a+d1:
                continue
            tmp1 += arr[x][y]
    return tmp1


def region4():
    tmp1 = 0
    cnt = -1
    for x in range(a+d2+1, N):
        cnt += 1
        for y in range(b+d2-cnt, N):
            if a+d1+d2 < x and y < b-d1+d2:
                continue
            tmp1 += arr[x][y]
    return tmp1


N = int(input())
total = 0
result = 100 * N * N
arr = [0] * N
for i in range(N):
    tmp = list(map(int, input().split()))
    arr[i] = tmp
    total += sum(tmp)

for a in range(N-2):
    for b in range(1, N-1):
        for d1 in range(1, b+1):
            for d2 in range(1, N-b):
                if 2 <= a+d1+d2 < N:
                    r1 = region1()
                    r2 = region2()
                    r3 = region3()
                    r4 = region4()
                    max_r = max(r1, r2, r3, r4, total-(r1+r2+r3+r4))
                    min_r = min(r1, r2, r3, r4, total-(r1+r2+r3+r4))
                    result = min(result, max_r-min_r)
                    print(result, a, b, d1, d2)
                if result == 0:break
            if result == 0: break
        if result == 0: break
    if result == 0: break

print(result)