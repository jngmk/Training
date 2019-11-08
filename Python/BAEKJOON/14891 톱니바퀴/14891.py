def rotate(ii, dd):
    global t, visited
    visited[ii] = 1
    if ii + 1 < 4 and not visited[ii+1]:
        if t[ii][2] != t[ii+1][6]:
            rotate(ii+1, dd*(-1))
    if ii - 1 >= 0 and not visited[ii-1]:
        if t[ii][6] != t[ii-1][2]:
            rotate(ii-1, dd*(-1))
    if dd == 1:
        tmp = t[ii].pop()
        t[ii][0:0] = tmp
    else:
        tmp = t[ii].pop(0)
        t[ii].append(tmp)


t = [0, 0, 0, 0]
for i in range(4):
    t[i] = list(input())
R = int(input())
for _ in range(R):
    idx, d = map(int, input().split())
    visited = [0, 0, 0, 0]
    rotate(idx-1, d)
result = 0
for i in range(4):
    if t[i][0] == '1':
        result += 2 ** i
print(result)
