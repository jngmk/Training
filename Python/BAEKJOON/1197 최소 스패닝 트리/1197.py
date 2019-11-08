def find_set(x):
    global p
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    global rank
    px, py = find_set(x), find_set(y)
    if rank[px] > rank[py]: px, py = py, px
    if rank[px] == rank[py]: rank[py] += 1
    p[px] = py


V, E = map(int, input().split())
lines = 0
h = []
p = list(range(V))
rank = [0] * V
w = 0
for _ in range(E):
    a, b, c = map(int, input().split())
    h.append([c, a-1, b-1])
h.sort(reverse=True)

while True:
    if lines == V-1: break
    c, a, b = h.pop()
    if find_set(a) == find_set(b): continue
    w += c
    lines += 1
    union(a, b)

print(w)
