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
    if flag:
        break
    # 1번말 부터 진행
    for i in range(K):
        print(turn, i)
        a, b, d = h[i]
        if flag:
            break
        # 해당말에 업혀있는 말만 움직임
        for k in range(len(board[a][b])):
            if board[a][b][k] == i:
                tmp = board[a][b][k:]
                board[a][b] = board[a][b][:k]
                # 진행방향 칸이 파란색(벽)일 때
                va, vb = a+da[d], b+db[d]
                if arr[va][vb] == 2:
                    h[i][2] = d = reverse_d(d)  # d ^= 1
                    # 반대방향 칸도 파란색(벽)일 때
                    if arr[a+da[d]][b+db[d]] == 2:
                        board[a][b].extend(tmp)
                        continue
                # 진행방향 칸이 흰색일 때
                va, vb = a + da[d], b + db[d]
                if arr[va][vb] == 0:
                    board[va][vb].extend(tmp)
                    # 좌표 갱신
                    for j in tmp:
                        h[j][0], h[j][1] = va, vb
                # 진행방향 칸이 빨간색일 때
                if arr[va][vb] == 1:
                    board[va][vb].extend((reversed(tmp)))
                    for j in tmp:
                        h[j][0], h[j][1] = va, vb
                if len(board[h[i][0]][h[i][1]]) >= 4:
                    flag = True
                    break
                break
    turn += 1

print(turn)
