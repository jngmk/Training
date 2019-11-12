import sys
sys.stdin = open('input.txt')

da, db = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    life_arr = [[0] * (2*K+M) for _ in range(2*K+M)]
    status_arr = [[0] * (2*K+M) for _ in range(2*K+M)]  # 0 번식가능공간, 1 비활성, 2 활성, 3 죽음
    cells, tmp_cells = {}, {}
    for a in range(N):
        tmp = list(map(int, input().split()))
        for b in range(M):
            life_arr[a+K][b+K] = tmp[b]
            if tmp[b] > 0:
                cells[(a+K, b+K, 1)] = tmp[b]  # 좌표, 생명력
                status_arr[a+K][b+K] = 1

    # K번 번식
    for _ in range(K):
        # print(_+1)
        for a, b, s in list(cells.keys()):
            l = cells[(a, b, s)]
            l -= 1
            # 비활성
            if s == 1:
                # 활성전환
                if l == 0:
                    cells.pop((a, b, 1))
                    cells[(a, b, 2)] = life_arr[a][b]
                    status_arr[a][b] = 2
                else:
                    cells[(a, b, s)] = l

            # 활성
            if s == 2:
                # 번식
                if l == life_arr[a][b]-1:
                    cells[(a, b, s)] = l
                    for d in range(4):
                        va, vb = a + da[d], b + db[d]
                        # 번식
                        if status_arr[va][vb] == 0:
                            if tmp_cells.get((va, vb, 1)):
                                if tmp_cells[(va, vb, 1)] < life_arr[a][b]:
                                    tmp_cells[(va, vb, 1)] = life_arr[a][b]
                            else:
                                tmp_cells[(va, vb, 1)] = life_arr[a][b]
                if l == 0:
                    cells.pop((a, b, s))
                    status_arr[a][b] = 3
                else:
                    cells[(a, b, s)] = l

        # 번식
        for a, b, s in list(tmp_cells.keys()):
            l = tmp_cells.pop((a, b, s))
            cells[(a, b, 1)] = l
            life_arr[a][b] = l
            status_arr[a][b] = 1

    print('#{} {}'.format(tc, len(cells)))
