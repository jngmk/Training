from itertools import combinations as comb

V = int(input())
arr = [[] for _ in range(V)]
result = 0
end_nodes = []
for _ in range(V):
    tmp = list(map(int, input().split()))
    t1 = tmp.pop(0) - 1
    if len(tmp) == 3: end_nodes.append(t1)
    while tmp:
        t2 = tmp.pop(0) - 1
        if t2 == -2: break
        t3 = tmp.pop(0)
        arr[t1].append((t2, t3))

two_nodes = list(comb(end_nodes, 2))
print(arr)
print(two_nodes)
