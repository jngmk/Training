def cleaning():
    global cleaned_space, d
    a, b = X, Y
    arr[a][b] = 2
    while True:
        flag = False
        for di in range(3, -1, -1):
            vd = (d+di) % 4
            va, vb = a+da[vd], b+db[vd]
            if not arr[va][vb]:
                arr[va][vb] = 2
                a, b = va, vb
                cleaned_space += 1
                d = vd
                flag = True
                break
        if not flag:
            if arr[a+da[(d+2)%4]][b+db[(d+2)%4]] == 1:
                return
            a, b = a+da[(d+2)%4], b+db[(d+2)%4]


da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
N, M = map(int, input().split())
X, Y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cleaned_space = 1
cleaning()

print(cleaned_space)
