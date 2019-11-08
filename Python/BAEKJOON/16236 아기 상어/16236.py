from collections import deque
from pprint import pprint


def sort_by_distance():
    global fishes
    for idx in range(len(fishes)):
        fishes[idx][0] = abs(fishes[idx][1] - shark[0]) + abs(fishes[idx][2] - shark[1])
    fishes.sort()


def can_reach(a, b):
    global tmp_times
    tmp_times = 0
    q = deque()
    visited = set()
    q.append([a, b, 0])
    while q:
        a, b, cnt = q.popleft()
        # 최소 거리로 이동
        if [a, b] == target:
            tmp_times = cnt
            return True
        for d in range(4):
            va, vb = a+da[d], b+db[d]
            if 0 <= va < N and 0 <= vb < N:
                # 크기가 더 큰 물고기는 지나가지 못함
                if arr[va][vb] > shark[2]:
                    continue
                if (va, vb) not in visited:
                    q.append([va, vb, cnt+1])
                    visited.add((va, vb))
    return False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
fishes = []
shark = 0
eat = 0
tot_times = 0
da, db = [0, 0, -1, 1], [-1, 1, 0, 0]
# 물고기 추가
for i in range(N):
    for j in range(N):
        if 0 < arr[i][j] <= 6:
            fishes.append([0, i, j, arr[i][j]])  # 거리, 세로 좌표, 가로 좌표, 크기
        if arr[i][j] == 9:
            shark = [i, j, 2]
# 거리 추가
sort_by_distance()

# 포식 시작
while True:
    # print(fishes, shark)
    min_target = target = [-1, -1]
    target_idx = -1
    flag = True
    tmp_times = 0
    min_times = N * N
    for f in range(len(fishes)):
        # 물고기 크기가 >= 상어 크기
        if fishes[f][3] >= shark[2]:
            continue
        # 먹을 수 있는 물고기 색출
        target = [fishes[f][1], fishes[f][2]]
        # print(target)
        # target_idx = f
        # print(target_idx)
        # 도달할 수 없다면
        if not can_reach(shark[0], shark[1]):
            continue
        # 움직인 거리가 지금까지 저장된 거리보다 짧고 최소거리와 같다면
        if tmp_times < min_times and tmp_times == fishes[f][0]:
            # tot_times += tmp_times
            min_times = tmp_times
            min_target, target_idx = target, f
            flag = False
            break
        # 돌아서 도착한다면
        if tmp_times < min_times:
            min_target, target_idx = target, f
            min_times = tmp_times
        elif tmp_times == min_times:
            if min_target[0] > target[0]:
                min_target, target_idx = target, f
            elif min_target[0] == target[0] and min_target[1] > target[1]:
                min_target, target_idx = target, f

    # 먹을 물고기가 없다면
    if min_target == [-1, -1]:
        break

    tot_times += min_times
    eat += 1
    # print(shark[2])
    # 크기만큼 먹었다면
    if eat == shark[2]:
        eat = 0
        shark[2] += 1
    # 물고기 제거, 상어 좌표 수정
    arr[shark[0]][shark[1]] = 0
    shark[0], shark[1] = fishes[target_idx][1], fishes[target_idx][2]
    arr[shark[0]][shark[1]] = 9
    fishes.pop(target_idx)

    # 수정된 상어 좌표로 재정렬
    sort_by_distance()
    # pprint(arr)

print(tot_times)
