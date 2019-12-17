import sys
input = sys.stdin.readline


def dfs(stack, idx):
    global find
    if find: return
    if not stack: return
    v = stack.pop()
    if v == b: find = True; return

    for nv in arr[v][idx]:
        if visited[nv]: continue
        visited[nv] = 1
        dfs(stack+[nv], idx)


N, K = map(int, input().split())
arr = [[[], []] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a][1].append(b)
    arr[b][0].append(a)
S = int(input())
for _ in range(S):
    a, b = map(int, input().split())
    visited = [0] * (N + 1)
    # 전후관계
    find = False
    dfs([a], 0)
    if find: print(1); continue
    dfs([a], 1)
    if find: print(-1); continue
    print(0)
