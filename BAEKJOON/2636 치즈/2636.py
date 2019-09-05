'''
강사님 코드
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



# 공기 2로 표시하기
def step1(x, y):
    q = []
    q.append((x, y))
    mat[x][y] = 2

    while q:
        x, y = q.pop(0)

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if not (0 <= xx < N and 0 <= yy < M): continue
            if mat[xx][yy] == 0 :
                mat[xx][yy] = 2
                q.append((xx, yy))



# 치즈의 공기와 접촉된 면을 표시하기 3, 치즈 내부 4
def step2(x, y):
    q = []

    mat[x][y] = 4
    if mat[x + 1][y] == 2 or mat[x - 1][y] == 2 or mat[x][y + 1] == 2 or mat[x][y - 1] == 2:
        mat[x][y] = 3

    q.append((x, y))
    while q:
        x, y = q.pop(0)

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if mat[xx][yy] == 1 :
                mat[xx][yy] = 4
                if mat[xx + 1][yy] == 2 or mat[xx - 1][yy] == 2 or mat[xx][yy + 1] == 2 or mat[xx][yy - 1] == 2:
                    mat[xx][yy] = 3
                q.append((xx, yy))


# 치즈 녹이기, 자료 재 정리, 치지 개수 반환
def step3():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 2: mat[i][j] = 0
            elif mat[i][j] == 3: mat[i][j] = 0; cnt += 1
            elif mat[i][j] == 4: mat[i][j] = 1; cnt += 1

    return cnt


N, M = map(int, input().split())

mat = [0] * N
for i in range(N):
    mat[i] = list(map(int, input().split()))

cheeze = 1
cnt = 0
while cheeze:
    step1(0, 0)
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                step2(i, j)
    last_cheeze = cheeze
    cheeze = step3()
    cnt += 1


print(cnt - 1)
print(last_cheeze)

'''