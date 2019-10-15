N, M, K = map(int, input().split())
S2D2 = [list(map(int, input().split())) for _ in range(N)]
soil = [[5] * N for _ in range(N)]
alive_tree = [[99, 99, 0]]
dead_tree = []
breeding = []
nutrition = 0
flag = False
da = [-1, -1, -1, 0, 0, 1, 1, 1]
db = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    a, b, age = map(int, input().split())
    alive_tree.append([a-1, b-1, age])

for _ in range(K):
    alive_tree.sort(reverse=True)
    print(alive_tree)
    print(soil)
    # spring
    tmp = len(alive_tree)
    for idx in range(tmp-1, 0, -1):
        a, b, age = alive_tree[idx]
        if soil[a][b] >= age:
            soil[a][b] -= age
            alive_tree[idx][2] += 1
            if age == 4:
                for d in range(8):
                    if 0 <= a + da[d] < N and 0 <= b + db[d] < N:
                        breeding.append([a + da[d], b + db[d], 1])
        else:
            nutrition += age // 2
            aa, bb, gg = alive_tree[idx-1]
            alive_tree.pop(idx)
            if aa > a or (aa == a and bb > b):
                flag = True
        if flag:
            soil[a][b] += nutrition
            nutrition = 0
            flag = False
        # soil[a][b] += S2D2[a][b]

    # print('spring', alive_tree)
    # print('spring', dead_tree)
    # print('spring', soil)

    # # summer
    # while dead_tree:
    #     a, b, age = dead_tree.pop()
    #     soil[a][b] += age // 2

    # print('summer', soil)

    # fall
    alive_tree.extend(breeding)
    breeding = []

    # winter
    for i in range(N):
        for j in range(N):
            soil[i][j] += S2D2[i][j]

    print(len(alive_tree)-1)
