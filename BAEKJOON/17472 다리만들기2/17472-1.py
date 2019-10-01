# 범위 확인 함수
def is_wall(aa, bb):
    if 0 <= aa < N and 0 <= bb < M:
        return False
    return True


# arr에 섬을 표시하면서 섬의 개수 카운팅
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


# 한 섬에서 다른 섬으로 갈 수 있는 최소길이를 배열에 저장
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


# 프림 알고리즘(최소 신장 트리) 적용
def prim(n):
    global min_distance, island_visited, impossible
    island_visited[n] = 1
    if sum(island_visited) == island_idx:
        return
    next_idx = 7
    temp_distance = 99
    # 확인된 노드를 살피며 지금 노드에서 다른 노드로 가는 것이 최선인지 확인
    for near in range(1, island_idx+1):
        flag = False
        # 프림 리스트 최소 거리로 갱신
        if prim_list[near][0] > distances[n][near]:
            prim_list[near][0] = distances[n][near]
            prim_list[near][1] = n
            flag = True
    if flag:  # 현재 노드에서 움직이는 것이 최적
        for near_idx in range(1, island_idx+1):
            if island_visited[near_idx]:
                continue
            if prim_list[near][1] != n:
                continue
            if temp_distance > prim_list[near_idx][0]:
                temp_distance = prim_list[near_idx][0]
                next_idx = near_idx
        if temp_distance == 99:
            impossible = True
            return
        min_distance += temp_distance
        prim(next_idx)
    else:  # 다른 노드에 최적의 간선이 있음
        for near_idx in range(1, island_idx+1):
            if island_visited[near_idx]:
                continue
            if temp_distance > prim_list[near_idx][0]:
                temp_distance = prim_list[near_idx][0]
                next_idx = near_idx
        if temp_distance == 99:
            impossible = True
            return
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
impossible = False
# 섬 개수 확인 및 표시
for a in range(N):
    for b in range(M):
        if arr[a][b] == 1:
            island_pos.append((a, b))
            island_idx += 1
            island(a, b, -island_idx)

distances = [[99] * (island_idx+1) for _ in range(island_idx+1)]  # 섬 간의 거리
island_visited = [0] * (island_idx+1)  # 방문한 섬 표시
prim_list = [[99, None] for _ in range(island_idx+1)]  # 프림 알고리즘 적용을 위한 배열 [해당 노드로 가는 최소 거리, 부모노드]

# 각 섬의 좌표 저장
for i in range(1, island_idx):
    i1, i2 = island_pos[i]
    bridge(i1, i2)

# 프림 알고리즘 실행
for idx in range(1, island_idx+1):
    prim(idx)
    break

# 불가능한 경우 색출
if min_distance == 0 or impossible:
    min_distance = -1

print(min_distance)
