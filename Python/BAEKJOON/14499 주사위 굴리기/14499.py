N, M, a, b, K = map(int, input().split())
arr = [0] * N
for idx in range(N):
    tmp = list(map(int, input().split()))
    arr[idx] = tmp
moves = list(map(int, input().split()))
da, db = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
bottom_top = {1: 6, 6: 1, 2: 5, 5: 2, 4: 3, 3: 4}
dice = [0] * 7  # top, up, right, left, down, bot

for d in moves:
    # 주사위 이동
    va, vb = a+da[d], b+db[d]
    # 보드 범위를 넘어가면 무시
    if not (0 <= va < N and 0 <= vb < M):
        continue
    if d == 1: dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif d == 2: dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif d == 3: dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    else: dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    # 이동한 칸의 값에 따른 값 조정
    if arr[va][vb] == 0:
        arr[va][vb] = dice[6]
    else:
        dice[6] = arr[va][vb]
        arr[va][vb] = 0
    a, b = va, vb
    print(dice[1])
