from pprint import pprint

R, C, T = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(R)]
dusts = {}
M = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def circulation(tr, tc, t_dense):
    global temp_dic
    if tc == 1:
        if 1 <= tr+1 <= M[0]:
            if tr+1 != M[0]:
                temp_dic.update({(tr+1, tc): t_dense})
        elif M[1] <= tr-1 <= R:
            if tr-1 != M[1]:
                temp_dic.update({(tr-1, tc): t_dense})
    elif tc == C:
        if tr == 1 or tr == R:
            temp_dic.update({(tr, tc-1): t_dense})
        elif 1 <= tr-1 < M[0]:
            temp_dic.update({(tr-1, tc): t_dense})
        elif M[1] < tr+1 <= R:
            temp_dic.update({(tr+1, tc): t_dense})
    else:
        if tr == M[0] or tr == M[1]:
            temp_dic.update({(tr, tc+1): t_dense})
        elif tr == 1 or tr == R:
            temp_dic.update({(tr, tc-1): t_dense})
        else:
            temp_dic.update({(tr, tc): t_dense})


for r in range(R):
    for c in range(C):
        if array[r][c] > 0:
            dusts.update({(r+1, c+1): array[r][c]})
        elif array[r][c] == -1:
            M.append(r+1)

for _ in range(T):
    # 확산
    dusts_list = list(dusts.keys())
    temp_list = []
    for r, c in dusts_list:
        m = dusts.get((r, c))
        cnt = 0
        for d in range(4):
            rr = r + dr[d]
            cc = c + dc[d]
            if 1 <= rr <= R and 1 <= cc <= C and array[rr-1][cc-1] != -1:
                temp_list.append((rr, cc, int(m / 5)))
                cnt += 1
        temp_list.append((r, c, -(int(m / 5) * cnt)))

    for rr, cc, dense in temp_list:
        if dusts.get((rr, cc)):
            dusts[(rr, cc)] += dense
        else:
            dusts.update({(rr, cc): dense})

    # # 프린트
    # printing = [[0] * C for _ in range(R)]
    # for pos, dense in dusts.items():
    #     r, c = pos
    #     printing[r - 1][c - 1] = dense
    #
    # pprint(printing)

    # 순환
    temp_dic = {}
    for pos, dense in dusts.items():
        r, c = pos
        circulation(r, c, dense)
    dusts = temp_dic

    # # 프린트
    # printing = [[0] * C for _ in range(R)]
    # for pos, dense in dusts.items():
    #     r, c = pos
    #     printing[r-1][c-1] = dense
    #
    # pprint(printing)

# 남은 먼지의 양
amount = 0
for dense in dusts.values():
    amount += dense

print(amount)

s = sorted(list_name, key=lambda list_in_arr: list_in_arr[-1])
