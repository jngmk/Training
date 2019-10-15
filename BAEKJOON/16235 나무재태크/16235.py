N, M, K = map(int, input().split())
S2D2 = [list(map(int, input().split())) for _ in range(N)]
soil = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
dead_tree = []
breeding = [[[] for _ in range(N)] for _ in range(N)]
da = [-1, -1, -1, 0, 0, 1, 1, 1]
db = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    a, b, age = map(int, input().split())
    trees[a-1][b-1].append(age)

for _ in range(K):
    # spring
    print(trees)
    print(soil)
    for a in range(N):
        for b in range(N):
            tmp = len(trees[a][b])
            idx = -1
            for age in range(tmp-1, -1, -1):
                if soil[a][b] >= trees[a][b][age]:
                    soil[a][b] -= trees[a][b][age]
                    trees[a][b][age] += 1
                    if trees[a][b][age] == 5:
                        for d in range(8):
                            if 0 <= a + da[d] < N and 0 <= b + db[d] < N:
                                breeding[a+da[d]][b+db[d]].append(1)
                else:
                    idx = age
                    break
            if idx >= 0:
                for age in range(idx, -1, -1):
                    soil[a][b] += trees[a][b][age]//2
                    trees[a][b].pop(age)
            soil[a][b] += S2D2[a][b]

    for a in range(N):
        for b in range(N):
            if breeding[a][b]:
                trees[a][b].extend(breeding[a][b])
                breeding[a][b] = []

result = 0
for a in range(N):
    for b in range(N):
        result += len(trees[a][b])

print(result)
