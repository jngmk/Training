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

print(distances)
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
min_distance = 999999


def perm(k, h0, temp, sur_ch):
    global result, min_distance
    if k == len(houses):
        temp1 = 0
        for r in temp:
            a1, b1 = r
            temp1 += distances[a1][b1]
        if min_distance > temp1:
            min_distance = temp1
    else:
        for i in range(h0+1, len(houses)):
            for j in sur_ch:
                perm(k+1, i, temp+[(i, j)], sur_ch)


for sur in survive_chic:
    # print('s', sur)
    perm(0, -1, [], sur)

print(result)
print(min_distance)
