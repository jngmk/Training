import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    tmp = list(input())[:-1]
    keys = [] if tmp == ['0'] else list(map(ord, tmp))
    visited = [[-1] * W for _ in range(H)]
    vst = 0
    pivot1, pivot2 = ord('a')-1, ord('a') - ord('A')
    steal = 0
    for k in keys:
        vst |= 1 << (k - pivot1)

    q = deque()
    while True:
        remain = False
        # 입구 찾기
        gates = []
        for w in range(W):
            for h in range(H):
                if w == 0 or w == W - 1 or h == 0 or h == H - 1:
                    if arr[h][w] == '*':
                        continue
                    elif arr[h][w] == '.':
                        gates.append((h, w))
                    elif 97 <= ord(arr[h][w]) <= 122:
                        gates.append((h, w))
                        keys.append(ord(arr[h][w]))
                        vst |= 1 << (ord(arr[h][w]) - pivot1)
                        arr[h][w] = '.'
                    elif 65 <= ord(arr[h][w]) <= 90 and ord(arr[h][w]) + pivot2 in keys:
                        arr[h][w] = '.'
                        gates.append((h, w))
                    elif arr[h][w] == '$':
                        steal += 1
                        gates.append((h, w))
                        arr[h][w] = '.'

        for gate in gates:
            g1, g2 = gate
            if vst == visited[g1][g2]: continue
            if vst | visited[g1][g2] == vst or visited[g1][g2] == -1:
                q.append((g1, g2))
                visited[g1][g2] = vst
                remain = True

        if not remain: break

        while q:
            # print(q)
            v1, v2 = q.popleft()
            for dv1, dv2 in (0, 1), (0, -1), (1, 0), (-1, 0):
                nv1, nv2 = v1+dv1, v2+dv2
                if not (0 <= nv1 < H and 0 <= nv2 < W): continue
                if vst == visited[nv1][nv2]: continue
                if vst | visited[nv1][nv2] == vst or visited[nv1][nv2] == -1:
                    if arr[nv1][nv2] == '*': continue
                    elif arr[nv1][nv2] == '.':
                        q.append((nv1, nv2))
                        visited[nv1][nv2] = vst
                    elif 97 <= ord(arr[nv1][nv2]) <= 122:
                        q.append((nv1, nv2))
                        keys.append(ord(arr[nv1][nv2]))
                        vst |= 1 << (ord(arr[nv1][nv2]) - pivot1)
                        arr[nv1][nv2] = '.'
                        visited[nv1][nv2] = vst
                    elif 65 <= ord(arr[nv1][nv2]) <= 90 and ord(arr[nv1][nv2]) + pivot2 in keys:
                        arr[nv1][nv2] = '.'
                        q.append((nv1, nv2))
                        visited[nv1][nv2] = vst
                    elif arr[nv1][nv2] == '$':
                        steal += 1
                        arr[nv1][nv2] = '.'
                        q.append((nv1, nv2))
                        visited[nv1][nv2] = vst
            # for ar in visited:
            #     print(ar)
            # print()

    print(steal)
    break
