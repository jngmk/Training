def row_func():
    global row, col, arr
    print(row, col)
    tmp_col = col
    col = 0
    for rr in range(row):
        tmpl = [[], [0] * 101]
        tmp = []
        for cc in range(100):
            if cc >= tmp_col and not arr[rr][cc]:
                break
            if not arr[rr][cc] in tmpl[0] and arr[rr][cc]:
                tmpl[0].append(arr[rr][cc])
            tmpl[1][arr[rr][cc]] += 1
        for idx in tmpl[0]:
            tmp.append([tmpl[1][idx], idx])
        tmp = sorted(tmp)
        length = len(tmp)
        print(tmp)
        col = max(col, 2*length)
        for ii in range(50):
            if ii < length:
                i1, i2 = tmp[ii]
                arr[rr][2*ii], arr[rr][2*ii+1] = i2, i1
            elif arr[rr][2*ii]:
                arr[rr][2*ii], arr[rr][2*ii+1] = 0, 0
            else:
                break


def col_func():
    global row, col, arr
    print(row, col)
    tmp_row = row
    row = 0
    for cc in range(col):
        tmpl = [[], [0] * 101]
        tmp = []
        for rr in range(100):
            if rr >= tmp_row and not arr[rr][cc]:
                break
            if not arr[rr][cc] in tmpl[0] and arr[rr][cc]:
                tmpl[0].append(arr[rr][cc])
            tmpl[1][arr[rr][cc]] += 1
        for idx in tmpl[0]:
            tmp.append([tmpl[1][idx], idx])
        tmp = sorted(tmp)
        length = len(tmp)
        print(tmp)
        row = max(row, 2*length)
        for ii in range(50):
            if ii < length:
                i1, i2 = tmp[ii]
                arr[2*ii][cc], arr[2*ii+1][cc] = i2, i1
            elif arr[2*ii][cc]:
                arr[2*ii][cc], arr[2*ii+1][cc] = 0, 0
            else:
                break


r, c, k = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    x, y, z = map(int, input().split())
    arr[i][0], arr[i][1], arr[i][2] = x, y, z
row = col = 3
cnt = 0
# row_func()
# print(arr)
# col_func()
# print(arr)
# print(row, col)
while True:
    # print(r-1, c-1, arr[r-1][c-1], k)
    if cnt > 100:
        cnt = -1
        break
    if arr[r-1][c-1] == k:
        break
    cnt += 1
    row_func() if row >= col else col_func()
    print(arr)
print(cnt)
