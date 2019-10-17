from collections import deque


def straight(aa, bb, dd):
    while True:
        if arr[aa+da[dd]][bb+db[dd]] == '.':
            aa = aa+da[dd]
            bb = bb+da[dd]
        elif arr[aa+da[dd]][bb+db[dd]] == 'O':
            return -1, -1
        else:
            return aa, bb


def bfs():
    global result
    q.append((r1, r2, b1, b2, 0))
    while True:
        if result != -1:
            break
        if not q:
            break
        ra, rb, ba, bb, cnt = q.popleft()
        for d in range(4):
            vra, vrb = straight(ra, rb, d)
            # print(vra, vrb)
            vba, vbb = straight(ba, bb, d)
            arr[vra][vrb] = 'R'
            arr[vba][vbb] = 'B'
            print(vra, vrb, vba, vbb)
            if vra == vrb == vba == vbb == -1:
                break
            elif vra == vrb == -1:
                result = cnt
                break
            if not r_visited[(vra, vrb)] and not b_visited[(vba, vbb)]:
                q.append((vra, vrb, vba, vbb, cnt+1))
                r_visited[(vra, vrb)] = 1
                b_visited[(vba, vbb)] = 1
            arr[vra][vrb] = '.'
            arr[vba][vbb] = '.'


da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
q = deque()
tmp_cnt = 0
result = -1
r_visited = {(i, j): 0 for i in range(1, N-1) for j in range(1, M-1)}
b_visited = {(i, j): 0 for i in range(1, N-1) for j in range(1, M-1)}
print(r_visited)
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
bfs()
# 탐색
print(result)
