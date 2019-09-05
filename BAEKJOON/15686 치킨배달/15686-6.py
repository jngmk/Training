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


def perm(temp, sur_ch):
    global result
    for h in range(len(houses)):
        hh = 99999
        for c in sur_ch:
            h1, h2 = houses[h]
            c1, c2 = chickens[c]
            distance = abs(h1 - c1) + abs(h2 - c2)
            if distance < hh:
                hh = distance
        temp += hh
    result.append(temp)


for a in range(N):
    for b in range(N):
        if array[a][b] == 1:
            houses.append((a, b))
        elif array[a][b] == 2:
            chickens.append((a, b))

survive(0, -1, [])
for sur in survive_chic:
    perm(0, sur)

min_distance = min(result)
print(min_distance)
