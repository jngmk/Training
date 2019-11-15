# 크루스칼, MST 랑 최단경로랑 다름
def find_set(x):
    global p
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    global rank, p
    px, py = find_set(x), find_set(y)
    if rank[px] == rank[py]:
        rank[py] += 1
    elif rank[px] > rank[py]:
        px, py = py, px
    p[px] = py


def kruskal(arr):
    global result
    n = 1
    while n < N-1:
        cc, aa, bb = arr.pop()
        if find_set(aa) == find_set(bb): continue
        if (a, b) == (aa, bb) or (b, a) == (aa, bb):continue
        union(aa, bb)
        result += cc
        n += 1


N, E = map(int, input().split())
p = [i for i in range(N+1)]
rank = [0] * (N+1)
h = []
for _ in range(E):
    a, b, c = map(int, input().split())
    if (1, N) == (a, b) or (N, 1) == (a, b): continue
    h.append([c, a, b])
a, b = map(int, input().split())

h.sort(reverse=True)
for cc, aa, bb in h:
    # print(a, b, aa, bb)
    if (a, b) == (aa, bb) or (b, a) == (aa, bb):
        result = cc
        kruskal(h)
        print(result)
        break
else:
    print(-1)
