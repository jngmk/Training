from collections import deque


def straight(aa, bb, dd):
    while True:
        # print(aa, bb)
        if arr[aa+da[dd]][bb+db[dd]] == '.':
            aa = aa+da[dd]
            bb = bb+db[dd]
        elif arr[aa+da[dd]][bb+db[dd]] == 'O':
            return -1, -1
        else:
            break
    return aa, bb


# def bfs():
#     global result
#     q.append((r1, r2, b1, b2, 1))
#     while True:
#         # print(q)
#         if result != -1:
#             break
#         if not q:
#             break
#         rr1, rr2, bb1, bb2, cnt = q.popleft()
#         # print('-----------------')
#         # print('pop', rr1, rr2, bb1, bb2)
#         for d in range(4):
#             if d == 0:
#                 if rr1 >= bb1:
#                     vba, vbb = straight(bb1, bb2, d)
#                     arr[vba][vbb] = 'B'
#                     vra, vrb = straight(rr1, rr2, d)
#                     arr[vra][vrb] = 'R'
#                 else:
#                     vra, vrb = straight(rr1, rr2, d)
#                     arr[vra][vrb] = 'R'
#                     vba, vbb = straight(bb1, bb2, d)
#                     arr[vba][vbb] = 'B'
#             elif d == 1:
#                 if bb2 >= rr2:
#                     vba, vbb = straight(bb1, bb2, d)
#                     arr[vba][vbb] = 'B'
#                     vra, vrb = straight(rr1, rr2, d)
#                     arr[vra][vrb] = 'R'
#                 else:
#                     vra, vrb = straight(rr1, rr2, d)
#                     arr[vra][vrb] = 'R'
#                     vba, vbb = straight(bb1, bb2, d)
#                     arr[vba][vbb] = 'B'
#             elif d == 2:
#                 if bb1 >= rr1:
#                     vba, vbb = straight(bb1, bb2, d)
#                     arr[vba][vbb] = 'B'
#                     vra, vrb = straight(rr1, rr2, d)
#                     arr[vra][vrb] = 'R'
#                 else:
#                     vra, vrb = straight(rr1, rr2, d)
#                     arr[vra][vrb] = 'R'
#                     vba, vbb = straight(bb1, bb2, d)
#                     arr[vba][vbb] = 'B'
#             else:
#                 if rr2 >= bb2:
#                     vba, vbb = straight(bb1, bb2, d)
#                     arr[vba][vbb] = 'B'
#                     vra, vrb = straight(rr1, rr2, d)
#                     arr[vra][vrb] = 'R'
#                 else:
#                     vra, vrb = straight(rr1, rr2, d)
#                     arr[vra][vrb] = 'R'
#                     vba, vbb = straight(bb1, bb2, d)
#                     arr[vba][vbb] = 'B'
#             # print(arr)
#             # print(vra, vrb, vba, vbb, d)
#             if vba == vbb == -1:
#                 break
#             elif vra == vrb == -1:
#                 result = cnt
#                 break
#             if not r_visited[(vra, vrb)] or not b_visited[(vba, vbb)]:
#                 q.append((vra, vrb, vba, vbb, cnt+1))
#                 r_visited[(vra, vrb)] = 1
#                 b_visited[(vba, vbb)] = 1
#             arr[vra][vrb] = '.'
#             arr[vba][vbb] = '.'


def dfs(rr1, rr2, bb1, bb2, cnt):
    global result, arr
    # print(q)
    if result <= cnt:
        return
    if bb1 == bb2 == -1:
        result = -1
        return
    if rr1 == rr2 == -1:
        result = cnt
        return
    print('-----------------')
    print('pop', rr1, rr2, bb1, bb2)
    for d in range(4):
        if d == 0:
            if rr1 >= bb1:
                vba, vbb = straight(bb1, bb2, d)
                arr[vba][vbb] = 'B'
                vra, vrb = straight(rr1, rr2, d)
                arr[vra][vrb] = 'R'
            else:
                vra, vrb = straight(rr1, rr2, d)
                arr[vra][vrb] = 'R'
                vba, vbb = straight(bb1, bb2, d)
                arr[vba][vbb] = 'B'
        elif d == 1:
            if bb2 >= rr2:
                vba, vbb = straight(bb1, bb2, d)
                arr[vba][vbb] = 'B'
                vra, vrb = straight(rr1, rr2, d)
                arr[vra][vrb] = 'R'
            else:
                vra, vrb = straight(rr1, rr2, d)
                arr[vra][vrb] = 'R'
                vba, vbb = straight(bb1, bb2, d)
                arr[vba][vbb] = 'B'
        elif d == 2:
            if bb1 >= rr1:
                vba, vbb = straight(bb1, bb2, d)
                arr[vba][vbb] = 'B'
                vra, vrb = straight(rr1, rr2, d)
                arr[vra][vrb] = 'R'
            else:
                vra, vrb = straight(rr1, rr2, d)
                arr[vra][vrb] = 'R'
                vba, vbb = straight(bb1, bb2, d)
                arr[vba][vbb] = 'B'
        else:
            if rr2 >= bb2:
                vba, vbb = straight(bb1, bb2, d)
                arr[vba][vbb] = 'B'
                vra, vrb = straight(rr1, rr2, d)
                arr[vra][vrb] = 'R'
            else:
                vra, vrb = straight(rr1, rr2, d)
                arr[vra][vrb] = 'R'
                vba, vbb = straight(bb1, bb2, d)
                arr[vba][vbb] = 'B'
        print(arr)
        print(vra, vrb, vba, vbb, d)
        if vba == vbb == -1:
            result = -1
            return
        if vra == vrb == -1:
            result = cnt
            return
        if not r_visited[(vra, vrb)] or not b_visited[(vba, vbb)]:
            r_visited[(vra, vrb)] = 1
            b_visited[(vba, vbb)] = 1
            arr[vra][vrb] = '.'
            arr[vba][vbb] = '.'
            q.append((vra, vrb, vba, vbb, cnt+1))
            r_visited[(vra, vrb)] = 0
            b_visited[(vba, vbb)] = 0


da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
q = deque()
tmp_cnt = 0
# result = -1
result = 9999999
r_visited = {(i, j): 0 for i in range(1, N-1) for j in range(1, M-1)}
b_visited = {(i, j): 0 for i in range(1, N-1) for j in range(1, M-1)}
# print(r_visited)
# 시작 위치 저장
for a in range(1, N-1):
    for b in range(1, M-1):
        if tmp_cnt == 3:
            break
        if arr[a][b] == 'R':
            r1, r2 = a, b
            arr[a][b] = '.'
            r_visited.update({(a, b): 1})
            tmp_cnt += 1
        elif arr[a][b] == 'B':
            arr[a][b] = '.'
            b1, b2 = a, b
            b_visited.update({(a, b): 1})
            tmp_cnt += 1
        elif arr[a][b] == 'O':
            o1, o2 = a, b
            tmp_cnt += 1
    if tmp_cnt == 3:
        break
# print(arr)
# bfs()
dfs(r1, r2, b1, b2, 1)
# 탐색
print(result)
