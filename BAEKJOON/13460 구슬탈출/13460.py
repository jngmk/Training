from collections import deque


def straight(aa, bb, dd):
    while True:
        if arr[aa+da[dd]][bb+db[dd]] == '.':
            aa = aa+da[dd]
            bb = bb+db[dd]
        elif arr[aa+da[dd]][bb+db[dd]] == 'O':
            return -1, -1
        else:
            break
    return aa, bb


def bfs():
    global result
    q.append((r1, r2, b1, b2, 1))
    while True:
        if not q:
            break
        rr1, rr2, bb1, bb2, cnt = q.popleft()
        # print('pop', rr1, rr2, bb1, bb2)
        if cnt == 11:
            return
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
            if vba == vbb == -1:
                arr[vra][vrb] = '.'
                arr[vba][vbb] = '.'
                continue
            if vra == vrb == -1:
                result = cnt
                return
            if not visited.get((vra, vrb, vba, vbb)):
                q.append((vra, vrb, vba, vbb, cnt+1))
                visited.update({(vra, vrb, vba, vbb): 1})
            arr[vra][vrb] = '.'
            arr[vba][vbb] = '.'


da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
q = deque()
result = -1
visited = {}
# 시작 위치 저장
for a in range(1, N-1):
    for b in range(1, M-1):
        if arr[a][b] == 'R':
            r1, r2 = a, b
            arr[a][b] = '.'
        elif arr[a][b] == 'B':
            arr[a][b] = '.'
            b1, b2 = a, b
visited.update({(r1, r2, b1, b2): 1})
bfs()
print(result)
