def perm(k, temp):
    global rotate_order
    if k == K:
        rotate_order.append(temp)
    else:
        for i in range(K):
            if visited[i]:
                continue
            visited[i] = 1
            perm(k+1, temp+[i])
            visited[i] = 0


def rotate(a, b, c):
    global temp_arr
    for i in range(1, c+1):
        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        for j in range(2*i):
            temp1.append(temp_arr[a-i][b-i+j])
            temp2.append(temp_arr[a-i+j][b+i])
            temp3.append(temp_arr[a+i][b+i-j])
            temp4.append(temp_arr[a+i-j][b-i])
        for j in range(2*i):
            temp_arr[a-i][b-i+1+j] = temp1[j]
            temp_arr[a-i+1+j][b+i] = temp2[j]
            temp_arr[a+i][b+i-1-j] = temp3[j]
            temp_arr[a+i-1-j][b-i] = temp4[j]


def min_line():
    global result
    for i in range(N):
        result = min(result, sum(temp_arr[i]))


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rotate_order = []
rotate_list = []
visited = [0] * (K+1)
result = 99999
for _ in range(K):
    tmp = list(map(int, input().split()))
    rotate_list.extend([tmp])
perm(0, [])
for order in rotate_order:
    print(order)
    temp_arr = [[arr[x][y] for y in range(M)] for x in range(N)]
    for idx in order:
        x, y, g = rotate_list[idx]
        rotate(x-1, y-1, g)
        print(temp_arr)
    min_line()
print(result)
