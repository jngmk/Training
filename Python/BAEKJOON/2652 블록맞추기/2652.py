from collections import deque


def indexing(r, c):
    global idx, arr
    rr, cc = r, c
    idx += 1
    q = deque([[r, c]])
    arr[r][c] = idx
    while q:
        aa, bb = q.popleft()
        for da, db in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            va, vb = aa+da, bb+db
            if not (0 <= va < N and 0 <= vb < N): continue
            if arr[va][vb] == idx or arr[va][vb] == 0: continue
            arr[va][vb] = idx
            q.append([va, vb])
            rr, cc = max(rr, va), max(cc, vb)
    return rr-r+1, cc-c+1


def check():
    # 위, 아래, 왼쪽, 오른쪽
    if state == 1:
        tmp = [[0] * width for _ in range(height + v)]
        if width != u: return False
        for a in range(aaa, aaa - height - v, -1):
            for b in range(bbb, bbb-width, -1):
                if not (0 <= a < N and 0 <= b < N): return False
                ta, tb = aaa-a, bbb-b
                if not arr[a][b]: tmp[ta][tb] = 1
    elif state == 2:
        tmp = [[0] * width for _ in range(height + v)]
        if width != u: return False
        for a in range(aa, aa + height + v):
            for b in range(bb, bb + width):
                if not (0 <= a < N and 0 <= b < N): return False
                ta, tb = a - aa, b - bb
                if not arr[a][b]: tmp[ta][tb] = 1
    elif state == 3:
        tmp = [[0] * height for _ in range(width + v)]
        if height != u: return False
        for b in range(bbb, bbb - width - v, -1):
            for a in range(aa, aa + height):
                if not (0 <= a < N and 0 <= b < N): return False
                ta, tb = bbb - b, a - aa
                if not arr[a][b]: tmp[ta][tb] = 1
    elif state == 4:
        tmp = [[0] * height for _ in range(width + v)]
        if height != u: return False
        for b in range(bb, bb + width + v):
            for a in range(aaa, aaa - height, -1):
                if not (0 <= a < N and 0 <= b < N): return False
                ta, tb = b - bb, aaa - a
                if not arr[a][b]: tmp[ta][tb] = 1
    th = len(tmp)
    ph, pw = len(puzzle), len(puzzle[0])
    row = 0
    flag = False
    for a in range(th):
        if (a-row) >= ph: return False
        if not flag and sum(tmp[a]) == 0:
            row += 1
            continue
        flag = True
        for b in range(pw):
            if puzzle[a-row][b] != tmp[a][b]:
                return False
    return True


N = int(input())
u, v, w, x, y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
idx = 1
squares = []
puzzle = [[0] * u for _ in range(x+v)]
result = 0
result_arr = []

# 퍼즐
for a in range(x+v):
    for b in range(u):
        if a < x and w <= b < w+y:
            puzzle[a][b] = 1
        elif a >= x:
            puzzle[a][b] = 1

# 시작점, 가로, 세로 저장
for a in range(N):
    for b in range(N):
        if arr[a][b] == 1:
            height, width = indexing(a, b)
            squares.append([a, b, width, height])

# 어느쪽이 뚫려 있는지
for square in squares:
    aa, bb, width, height = square
    aaa, bbb = aa + height - 1, bb + width - 1
    # 위, 아래, 왼쪽, 오른쪽
    state = 0
    if state == 0:
        vaa, vbb = aaa, bbb
        va, vb = aa, bb
        for _ in range(width-1):
            # down
            vaa, vbb = vaa, vbb-1
            if arr[vaa][vbb] == 0:
                state = 2
                break
            # up
            va, vb = va, vb+1
            if arr[va][vb] == 0:
                state = 1
                break
    if state == 0:
        vaa, vbb = aaa, bbb
        va, vb = aa, bb
        for _ in range(height - 1):
            # right
            vaa, vbb = vaa-1, vbb
            if arr[vaa][vbb] == 0:
                state = 4
                break
            # left
            va, vb = va+1, vb
            if arr[va][vb] == 0:
                state = 3
                break
    if state == 0: continue
    if check():
        result += 1
        result_arr.append([aa, bb])

print(result)
for a, b in result_arr:
    print(a+1, b+1)
