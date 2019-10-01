def is_wall(aa, bb):
    if 0 <= aa < N and 0 <= bb < M:
        return False
    return True


def island(aa, bb, num):
    global arr
    temp_stack1 = [(aa, bb)]
    arr[aa][bb] = num
    while temp_stack1:
        t1, t2 = temp_stack1.pop()
        for d in range(4):
            if not is_wall(t1+da[d], t2+db[d]):
                if arr[t1+da[d]][t2+db[d]] == 1:
                    temp_stack1.append((t1+da[d], t2+db[d]))
                    arr[t1+da[d]][t2+db[d]] = num


def bridge(aa, bb):
    global distances
    temp_stack = [(aa, bb)]
    visited_arr[aa][bb] = 1
    while temp_stack:
        t1, t2 = temp_stack.pop()
        for d in range(4):
            temp_cnt = 0
            if not is_wall(t1 + da[d], t2 + db[d]) and not visited_arr[t1 + da[d]][t2 + db[d]]:
                if arr[t1 + da[d]][t2 + db[d]] == 0:
                    v1 = t1 + da[d]
                    v2 = t2 + db[d]
                    while True:
                        if is_wall(v1, v2):
                            break
                        if arr[v1][v2] == 0:
                            temp_cnt += 1
                        if arr[v1][v2] != 0 and temp_cnt == 1:
                            break
                        if arr[v1][v2] != 0 and temp_cnt > 1:
                            if -arr[v1][v2] > i:
                                distances[i][-arr[v1][v2]] = min(temp_cnt, distances[i][-arr[v1][v2]])
                                distances[-arr[v1][v2]][i] = min(temp_cnt, distances[i][-arr[v1][v2]])
                            break
                        v1 = v1 + da[d]
                        v2 = v2 + db[d]
                else:
                    temp_stack.append((t1 + da[d], t2 + db[d]))
                    visited_arr[t1 + da[d]][t2 + db[d]] = 1


def prim(n):
    global min_distance, island_visited
    island_visited[n] = 1
    if sum(island_visited) == island_idx:
        return
    # print(distances)
    # print(island_visited)
    # print(min_distance)
    next_idx = 7
    temp_distance = 99
    for near in range(1, island_idx+1):
        flag = False
        # print(prim_list)
        if prim_list[near][0] > distances[n][near]:
            prim_list[near][0] = distances[n][near]
            prim_list[near][1] = n
            flag = True
    if flag:
        for near_idx in range(1, island_idx+1):
            if island_visited[near_idx]:
                continue
            if prim_list[near][1] != n:
                continue
            if temp_distance > prim_list[near_idx][0]:
                temp_distance = prim_list[near_idx][0]
                next_idx = near_idx
        min_distance += temp_distance
        prim(next_idx)
    else:
        for near_idx in range(1, island_idx+1):
            if island_visited[near_idx]:
                continue
            if temp_distance > prim_list[near_idx][0]:
                temp_distance = prim_list[near_idx][0]
                next_idx = near_idx
        min_distance += temp_distance
        prim(next_idx)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited_arr = [[0] * M for _ in range(N)]
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
island_idx = 0
island_pos = [(0, 0)]
min_distance = 0
for a in range(N):
    for b in range(M):
        if arr[a][b] == 1:
            island_pos.append((a, b))
            island_idx += 1
            island(a, b, -island_idx)

distances = [[99] * (island_idx+1) for _ in range(island_idx+1)]
island_visited = [0] * (island_idx+1)
prim_list = [[99, None] for _ in range(island_idx+1)]

for i in range(1, island_idx):
    i1, i2 = island_pos[i]
    bridge(i1, i2)

for idx in range(1, island_idx+1):
    distances[idx][0] = min(distances[idx])

# print(distances)

for idx in range(1, island_idx+1):
    if distances[idx].count(distances[idx][0]) > 2:
        continue
    prim(idx)
    break

if min_distance == 0:
    min_distance = -1
print(island_pos)
print(min_distance)
