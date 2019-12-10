from collections import deque

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
ji = deque()
fire = deque()
cnt = 0
di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
escape = False

# 배열 정리
for r in range(R):
    for c in range(C):
        if arr[r][c] == '#': arr[r][c] = 1
        elif arr[r][c] == '.': arr[r][c] = 0
        elif arr[r][c] == 'J':
            arr[r][c] = 0
            ji.append([r, c])
        elif arr[r][c] == 'F':
            arr[r][c] = 1
            fire.append([r, c])

# 턴 구분
ji.append([-1, -1])
fire.append([-1, -1])

# 미로 탈출
while len(ji) != 1:
    # 불 번짐
    while True:
        f1, f2 = fire.popleft()
        if (f1, f2) == (-1, -1):
            fire.append([-1, -1])
            break
        for df1, df2 in di:
            nf1, nf2 = f1+df1, f2+df2
            if not (0 <= nf1 < R and 0 <= nf2 < C): continue
            if arr[nf1][nf2] == 1: continue
            arr[nf1][nf2] = 1
            fire.append([nf1, nf2])
    # 지훈 이동
    while True:
        j1, j2 = ji.popleft()
        if j1 == 0 or j1 == R-1 or j2 == 0 or j2 == C-1:
            escape = True
            break
        if (j1, j2) == (-1, -1):
            ji.append([-1, -1])
            break
        for dj1, dj2 in di:
            nj1, nj2 = j1+dj1, j2+dj2
            if not (0 <= nj1 < R and 0 <= nj2 < C): continue
            if arr[nj1][nj2] == 1 or arr[nj1][nj2] == 2: continue
            arr[nj1][nj2] = 2
            ji.append([nj1, nj2])

    cnt += 1

    if escape: break

print(cnt if escape else 'IMPOSSIBLE')
