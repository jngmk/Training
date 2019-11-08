from collections import deque


def rotate(x, d, k):
    global arr
    k %= M
    for i in range(1, N+1):
        # x의 배수일 때만 회전
        if i % x != 0:
            continue
        tmp = [0] * M
        # 반시계 방향 회전
        if d:
            for j in range(M):
                tmp[(j-k) % M] = arr[i-1][j]
            arr[i-1] = tmp
        # 시계 방향 회전
        else:
            for j in range(M):
                tmp[(j+k) % M] = arr[i-1][j]
            arr[i-1] = tmp


def calc():
    global arr, remains, arr_sum
    flag = False
    for a in range(N):
        for b in range(M):
            if arr[a][b] == 0:
                continue
            q = deque()
            t = arr[a][b]
            q.append((a, b))
            while q:
                va, vb = q.popleft()
                for dd in range(4):
                    vva, vvb = va+da[dd], vb+db[dd]
                    if vvb == -1: vvb = M-1
                    if vvb == M: vvb = 0
                    if 0 <= vva < N and 0 <= vvb < M:
                        if arr[vva][vvb] == t:
                            q.append((vva, vvb))
                            arr_sum -= t
                            arr[vva][vvb] = 0
                            remains[vva] -= 1
                            flag = True
    if arr_sum == 0:
        return

    if not flag:
        avg = arr_sum / sum(remains)
        for a in range(N):
            for b in range(M):
                if arr[a][b] == 0:
                    continue
                if arr[a][b] > avg:
                    arr[a][b] -= 1
                    arr_sum -= 1
                elif arr[a][b] < avg:
                    arr[a][b] += 1
                    arr_sum += 1


N, M, T = map(int, input().split())
arr_sum = 0
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr_sum += sum(temp)
    arr.append(temp)
remains = [M] * N
da, db = [0, 0, 1, -1], [1, -1, 0, 0]
for _ in range(T):
    xi, di, ki = map(int, input().split())
    rotate(xi, di, ki)
    calc()
    if arr_sum == 0:
        break

print(arr_sum)
