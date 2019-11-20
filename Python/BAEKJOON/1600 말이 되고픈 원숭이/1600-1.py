from collections import deque

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[K] * W for _ in range(W)]
result = 0

s1, s2 = 0, 0
g1, g2 = H-1, W-1

di4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
di8 = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
       (2, -1), (2, 1), (1, -2), (1, 2)]

q = deque([[s1, s2, K, 0]])
while q:
    h, w, k, cnt = q.popleft()
    if (h, w) == (g1, g2):
        result = cnt
        break
    for dh, dw in di4:
        vh, vw = h+dh, w+dw
        if not (0 <= vh < H and 0 <= vw < W): continue
        if arr[vh][vw]: continue
        if visited[vh][vw] < k: continue
        visited[vh][vw] = k
        q.append([vh, vw, k, cnt+1])
    if k:
        for dh, dw in di8:
            vh, vw = h+dh, w+dw
            if not (0 <= vh < H and 0 <= vw < W): continue
            if arr[vh][vw]: continue
            if visited[vh][vw] < k-1: continue
            visited[vh][vw] = k-1
            q.append([vh, vw, k-1, cnt+1])

print(result if result != 0 else -1)
