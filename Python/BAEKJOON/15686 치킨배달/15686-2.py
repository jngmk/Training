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

distances = [[0] * len(chickens) for _ in range(len(houses))]
for h in range(len(houses)):
    for c in range(len(chickens)):
        h1, h2 = houses[h]
        c1, c2 = chickens[c]
        distance = abs(h1-c1) + abs(h2-c2)
        distances[h][c] = distance

min_distance = 999999


def perm(k, now, temp, is_visited1, is_visited2):
    global min_distance
    if k == len(houses):
        if min_distance > temp and len(is_visited2) <= M:
            min_distance = temp
            # print(min_distance)
    else:
        for a1 in range(k, len(houses)):
            for b1 in range(len(chickens)):
                if (a1, b1) in is_visited1:
                    continue
                if b1 not in is_visited2:
                    if len(is_visited2) >= M:
                        continue
                    print(1111111111111, a1, b1)
                    perm(k+1, b1, temp+distances[a1][b1], is_visited1+[(a1, b1)], is_visited2+[b1])
                else:
                    print(222222222222, a1, b1)
                    perm(k+1, b1, temp + distances[a1][b1], is_visited1+[(a1, b1)], is_visited2)


perm(0, -1, 0, [], [])
print(min_distance)
