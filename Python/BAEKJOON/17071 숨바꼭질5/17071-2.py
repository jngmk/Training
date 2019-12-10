from collections import deque

n, k = map(int, input().split())
arr = [0] * 500001
visited = [[0] * 500001, [0] * 500001]
kk, nn, ans = 0, 0, -float('inf')
qk = deque([[k, kk + 1]])
qn = deque([[n, nn]])
find = True if n == k else False

if not find:
    # k 기록
    while True:
        k, kk = qk.popleft()
        if k + kk > 500000: break
        arr[k + kk] = -kk
        qk.append([k + kk, kk + 1])
    # 숨바꼭질
    while True:
        # print(qn)
        n, nn = qn.popleft()
        nc = (nn+1) % 2
        if nn >= kk: break
        if 2 * n <= 500000:
            if visited[nc][2*n] == 0:
                if arr[2 * n] < 0:
                    if (nn + 1) + arr[2 * n] <= 0 and ((nn + 1) + arr[2 * n]) % 2 == 0:
                        ans = max(arr[2 * n], ans)
                        kk = min(-arr[2 * n], kk)
                        find = True
                else:
                    arr[2 * n] = nn + 1
                visited[nc][2 * n] = 1
                qn.append([2 * n, nn + 1])
        if n + 1 <= 500000:
            if visited[nc][n+1] == 0:
                if arr[n + 1] < 0:
                    if (nn + 1) + arr[n + 1] <= 0 and ((nn + 1) + arr[n + 1]) % 2 == 0:
                        ans = max(arr[n + 1], ans)
                        kk = min(-arr[n + 1], kk)
                        find = True
                else:
                    arr[n + 1] = nn + 1
                visited[nc][n + 1] = 1
                qn.append([n + 1, nn + 1])
        if n - 1 > 0:
            if visited[nc][n-1] == 0:
                if arr[n - 1] < 0:
                    if (nn + 1) + arr[n - 1] <= 0 and ((nn + 1) + arr[n - 1]) % 2 == 0:
                        ans = max(arr[n - 1], ans)
                        kk = min(-arr[n - 1], kk)
                        find = True
                else:
                    arr[n - 1] = nn + 1
                visited[nc][n - 1] = 1
                qn.append([n - 1, nn + 1])

if ans == -float('inf'):
    ans = 0
print(-ans if find else -1)
