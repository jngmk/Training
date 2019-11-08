def dragon_curve(j, i, d, g):
    global arr, min_a, min_b, max_a, max_b
    # 진행방향 저장
    dd = [d]
    # 시작점, 끝점 설정
    arr[i][j] = 1
    ga, gb = i+da[d], j+db[d]
    arr[ga][gb] = 1
    sa, sb = ga, gb
    min_a, max_a = min(min_a, i, ga), max(max_a, i, ga)
    min_b, max_b = min(min_b, j, gb), max(max_b, i, gb)
    # pprint(arr)
    for _ in range(g):
        # 회전
        tmp = dd[:]
        tmp = rotate(tmp)[:]
        # 복제
        for d in tmp:
            ga, gb = sa+da[d], sb+db[d]
            arr[ga][gb] = 1
            dd.append(d)
            sa, sb = ga, gb
            min_a, max_a = min(min_a, sa), max(max_a, sa)
            min_b, max_b = min(min_b, sb), max(max_b, sb)


def rotate(directions):
    temp_d = list(reversed(directions))
    for idx in range(len(directions)):
        directions[idx] = (temp_d[idx]+1) % 4
    return directions


def count():
    global cnt
    for i in range(min_a, max_a):
        for j in range(min_b, max_b):
            if arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1] == 1:
                cnt += 1


N = int(input())
arr = [[0] * 101 for _ in range(101)]
cnt = 0
max_a = max_b = 0
min_a = min_b = 102
da, db = [0, -1, 0, 1], [1, 0, -1, 0]
for _ in range(N):
    b, a, di, gen = map(int, input().split())
    dragon_curve(b, a, di, gen)
count()
print(cnt)
