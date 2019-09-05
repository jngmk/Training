# 테케 오답, 시간 초과
N, M, K = map(int, input().split())
S2D2 = [list(map(int, input().split())) for _ in range(N)]
soil = [[5] * (N+1) for _ in range(N+1)]
trees = [[0] * (N+1) for _ in range(N+1)]
alive_tree = []
dead_tree = []
da = [-1, -1, -1, 0, 0, 1, 1, 1]
db = [-1, 0, 1, -1, 1, -1, 0, 1]

print(trees)
for _ in range(M):
    A, B, age = map(int, input().split())
    trees[A][0] += 1
    alive_tree.append((A, B))
    if trees[A][B] == 0:
        trees[A][B] = [age]
    else:
        trees[A][B].append(age)
print(trees)

for _ in range(K):
    # spring
    for i in range(len(alive_tree)-1, -1, -1):
        a, b = alive_tree[i]
        for t in range(len(trees[a][b])-1, -1, -1):
            if trees[a][b][t] > soil[a][b]:
                dead_tree.append((a, b, trees[a][b][t]//2))
                trees[a][b][t] = -99
                trees[a][0] -= 1
            else:
                if trees[a][b][t] > 0:
                    soil[a][b] -= trees[a][b][t]
            trees[a][b][t] += 1
    print('spring', trees)
    print('spring', soil)


    # summer
    for manure in dead_tree:
        a, b, m = manure
        soil[a][b] += m
    dead_tree = []
    print('summer', dead_tree)
    print('summer', soil)

    # fall
    for i in range(len(alive_tree)-1, -1, -1):
        a, b = alive_tree[i]
        for t in range(len(trees[a][b])-1, -1, -1):
            if trees[a][b][t] % 5 == 0:
                for d in range(8):
                    ra = a + da[d]
                    rb = b + db[d]
                    if 0 < ra < N and 0 < rb < N:
                        if trees[ra][rb] == 0:
                            trees[ra][rb] = [1]
                        else:
                            trees[ra][rb].append(1)
                        trees[ra][0] += 1
                        if (ra, rb) not in alive_tree:
                            alive_tree.append((ra, rb))
    print('fall', trees)

    # winter
    for a in range(N):
        for b in range(N):
            soil[a][b] += S2D2[a][b]

    print('winter', soil)

    result = 0
    for n in range(N+1):
        result += trees[n][0]

    print('result', result)
    print('---------------')
