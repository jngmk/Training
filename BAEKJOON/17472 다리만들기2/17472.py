# 제어 불능;


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


def bridge(aa, bb, cnt, idx):
    global visited_arr, island_visited, min_cnt, temp_minus, temp_idx
    if sum(island_visited) == island_idx-1:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    temp_stack[idx] = [(aa, bb)]
    visited_arr[aa][bb] = 1
    while temp_stack[idx]:
        t1, t2 = temp_stack[idx].pop()
        for d in range(4):
            temp_cnt = 0
            if not is_wall(t1 + da[d], t2 + db[d]) and not visited_arr[t1+da[d]][t2+db[d]]:
                if arr[t1 + da[d]][t2 + db[d]] == 0:
                    v1 = t1+da[d]
                    v2 = t2+db[d]
                    temp_cnt += 1
                    while True:
                        if is_wall(v1+da[d], v2+db[d]):
                            break
                        if arr[v1+da[d]][v2+db[d]] == 0:
                            temp_cnt += 1
                        if arr[v1+da[d]][v2+db[d]] != 0 and temp_cnt == 1:
                            break
                        if arr[v1+da[d]][v2+db[d]] != 0 and temp_cnt > 1 and not island_visited[-arr[v1+da[d]][v2+db[d]]]:
                            island_visited[-arr[v1+da[d]][v2+db[d]]] = 1
                            temp_idx[idx].append(-arr[v1+da[d]][v2+db[d]])
                            cnt += temp_cnt
                            temp_minus[idx] += temp_cnt
                            bridge(v1+da[d], v2+db[d], cnt, -arr[v1+da[d]][v2+db[d]])
                            break
                        v1 = v1+da[d]
                        v2 = v2+db[d]
                else:
                    temp_stack[idx].append((t1 + da[d], t2 + db[d]))
                    visited_arr[t1+da[d]][t2+db[d]] = 1
    print(idx)
    while temp_idx[idx]:
        i = temp_idx[idx].pop()
        island_visited[i] = 0
    cnt -= temp_minus[idx]
    temp_minus[idx] = 0
    print('-', island_visited, cnt, idx)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited_arr = [[0] * M for _ in range(N)]
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
island_idx = 1
min_cnt = 101
for a in range(N):
    for b in range(M):
        if arr[a][b] == 1:
            island_pos = (a, b)
            island(a, b, -island_idx)
            island_idx += 1

island_visited = [0] * island_idx
temp_idx = [[0] for _ in range(island_idx)]
temp_minus = [0] * island_idx
temp_stack = [[(0, 0)] for _ in range(island_idx)]
i1, i2 = island_pos
island_visited[-arr[i1][i2]] = 1
bridge(i1, i2, 0, -arr[i1][i2])
print(min_cnt)
