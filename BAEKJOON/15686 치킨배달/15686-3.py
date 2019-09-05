# 시간초과
N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []

for a in range(N):
    for b in range(N):
        if array[a][b] == 1:
            houses.append((a, b))
        elif array[a][b] == 2:
            chickens.append((a, b))
# print(houses)
# print(chickens)

distances = [[0] * len(chickens) for _ in range(len(houses))]
for h in range(len(houses)):
    for c in range(len(chickens)):
        h1, h2 = houses[h]
        c1, c2 = chickens[c]
        distance = abs(h1-c1) + abs(h2-c2)
        distances[h][c] = distance

# print(distances)
survive_chic = []
result = []


def survive(k, c0, temp):
    global survive_chic
    if k == M:
        survive_chic.append(temp)
    else:
        for j in range(c0+1, len(chickens)):
            survive(k+1, j, temp+[j])


survive(0, -1, [])
# print('sur', survive_chic)


def perm(k, h0, temp, sur_ch):
    global result
    if k == len(houses):
        result.append(temp)
    else:
        for i in range(h0+1, len(houses)):
            res_i = []
            for j in sur_ch:
                res_i.append(distances[i][j])
            min_i = min(res_i)
            perm(k+1, i, temp+min_i, sur_ch)


for sur in survive_chic:
    # print('s', sur)
    perm(0, -1, 0, sur)

# print(result)
min_distance = min(result)
print(min_distance)
