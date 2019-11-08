from pprint import pprint


def reverse_d(dd):
    reverse_dict = {0: 1, 1: 0, 2: 3, 3: 2}
    return reverse_dict[dd]


N, K = map(int, input().split())
arr = [[2] * (N+2)]
arr += [[2]+list(map(int, input().split()))+[2] for _ in range(N)]
arr += [[2] * (N+2)]
board = list([[] for _ in range(N+2)] for _ in range(N+2))
da, db = [0, 0, -1, 1], [1, -1, 0, 0]
h = []
turn = 0
for i in range(K):
    t1, t2, t3 = map(int, input().split())
    board[t1][t2].append(i)
    h.append([t1, t2, t3-1])
flag = False
while True:
    if turn > 1000:
        turn = -1
        break
    for hh in range(K):
        if len(board[h[hh][0]][h[hh][1]]) >= 4:
            flag = True
            break
    if flag:
        break
    # 1번말 부터 진행
    for i in range(K):
        a, b, d = h[i]
        # 맨 아래에 있는 말일 때 진행
        if board[a][b][0] != i:
            continue
        # 진행방향 칸이 파란색(벽)일 때
        va, vb = a+da[d], b+db[d]
        if arr[va][vb] == 2:
            h[i][2] = d = reverse_d(d)  # d ^= 1
            # 반대방향 칸도 파란색(벽)일 때
            if arr[a+da[d]][b+db[d]] == 2:
                continue
        # 진행방향 칸이 흰색일 때
        va, vb = a + da[d], b + db[d]
        if arr[va][vb] == 0:
            board[va][vb].extend(board[a][b])
            # 좌표 갱신
            for j in board[a][b]:
                h[j][0], h[j][1] = va, vb
            board[a][b] = []
        # 진행방향 칸이 빨간색일 때
        if arr[va][vb] == 1:
            board[va][vb].extend((reversed(board[a][b])))
            for j in board[a][b]:
                h[j][0], h[j][1] = va, vb
            board[a][b] = []
    pprint(board)
    turn += 1

print(turn)
