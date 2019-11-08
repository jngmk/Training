# V = int(input())
# arr = [[] for _ in range(V)]
# result = 0
# for _ in range(V):
#     tmp = list(map(int, input().split()))
#     t1 = tmp.pop(0) - 1
#     while tmp:
#         t2 = tmp.pop(0) - 1
#         if t2 == -2: break
#         t3 = tmp.pop(0)
#         arr[t1].append((t2, t3))
#
# for k in range(V):
#     for i in range(V):
#         if i == k: continue
#         for j in range(V):
#             if j == k or j == i: continue
#             arr[]