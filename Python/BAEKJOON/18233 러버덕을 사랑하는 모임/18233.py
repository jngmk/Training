def comb(k, c, choosen_people, minv_sum, maxv_sum):
    global presents, find, check
    print(choosen_people, find, check)
    if minv_sum > E: check = True; return
    if k == P:
        if minv_sum <= E <= maxv_sum:
            for p in choosen_people:
                presents[p] = group[p][0]
            remain_doll = E - minv_sum
            while True:
                if remain_doll <= 0: break
                for p in choosen_people:
                    if group[p][1] - presents[p] > 0:
                        gift = min(remain_doll, group[p][1] - presents[p])
                        presents[p] += gift
                        remain_doll -= gift
                    if remain_doll <= 0: break
            find = True
        return
    else:
        for n in range(c+1, N):
            if find: return
            if visited[n]: continue
            visited[n] = 1
            comb(k+1, n, choosen_people+[sorted_group[n][2]], minv_sum+sorted_group[n][0], maxv_sum+sorted_group[n][1])
            visited[n] = 0
            if check: check = False; print(k, choosen_people); return


N, P, E = map(int, input().split())
group = []
presents = [0] * N
for n in range(N):
    minv, maxv = map(int, input().split())
    group.append((minv, maxv, n))

sorted_group = sorted(group)

if sorted_group[0][0] + sorted_group[1][0] + sorted_group[2][0] > E:
    print(-1)
else:
    find = False
    check = False
    visited = [0] * N
    comb(0, -1, [], 0, 0)
    print(' '.join(map(str, presents)) if find else -1)

# 5 3 10
# 1 2
# 2 3
# 3 4
# 8 9
# 9 10