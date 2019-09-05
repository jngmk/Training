# 시간초과
N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []
survive_chic = []
result = []


def survive(k, c0, temp):
    global survive_chic
    if k == M:
        survive_chic.append(temp)
    else:
        for j in range(c0+1, len(chickens)):
            survive(k+1, j, temp+[j])


def perm(k, h0, temp, sur_ch):
    global result
    if k == len(houses):
        result.append(temp)
    else:
        for i in range(h0+1, len(houses)):
            i1, i2 = houses[i]
            res_i = []
            for j in sur_ch:
                j1, j2 = chickens[j]
                res_i.append(abs(i1-j1)+abs(i2-j2))
            min_i = min(res_i)
            perm(k+1, i, temp+min_i, sur_ch)

for a in range(N):
    for b in range(N):
        if array[a][b] == 1:
            houses.append((a, b))
        elif array[a][b] == 2:
            chickens.append((a, b))

survive(0, -1, [])
for sur in survive_chic:
    perm(0, -1, 0, sur)

min_distance = min(result)
print(min_distance)
