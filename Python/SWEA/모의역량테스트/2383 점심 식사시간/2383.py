# 시뮬로 불가능할 듯

import sys
sys.stdin = open('input.txt')
from collections import deque

da, db = [0, 0, -1, 1], [-1, 1, 0, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0, 0, 0]
    arr[0] = [list(map(int, input().split())) for _ in range(N)]
    people, stairs = [], []
    visited = {}
    minutes = 0
    tmp_i = 1
    for a in range(N):
        for b in range(N):
            if arr[0][a][b] == 1:
                people.append([0, a, b])
                arr[0][a][b] = 0
            elif arr[0][a][b] > 1:
                stairs.append([a, b])
                arr[tmp_i] = [arr[0][a][b], 0]  # 계단길이, 내려가는 사람 수
                arr[0][a][b] = tmp_i
                tmp_i += 1

    print(arr)
    P = len(people)
    completed_people = 0
    q = deque()
    q.append([people, []])
    while q:
        if completed_people == P: break
        people, stair_people = q.popleft()
        visited.add(tuple(sorted(people)))
        tmp_people = people[:]
        # 계단에 있을 때
        for p in range(len(stair_people)-1, -1, -1):
            k, i = stair_people[p]
            # 이동 완료
            if i == arr[k][0]-1:
                completed_people += 1
                arr[k][1] -= 1
                stair_people.pop(p)


        # 계단이 아닐 때
        for p in range(len(people)-1, -1, -1):
            k, a, b = people[p]
            if [a, b] not in stairs:
                for d in range(4):
                    va, vb = a+da[d], b+db[d]
                    if not (0 <= va < N and 0 <= vb < N): continue
                    tmp_people[p] = [k, va, vb]
                    sorted_tmp_people = tuple(sorted(tmp_people))
                    if sorted_tmp_people in visited: tmp_people[p] = [k, a, b]; continue
                    q.append(tmp_people)
                    visited.add(sorted_tmp_people)
            # 계단 입구일 때
            else:
                if arr[arr[k][a][b]][1] == 3:
                    continue
                else:
                    tmp_people[p] = [arr[k][a][b], 0]
                    sorted_tmp_people = tuple(sorted(tmp_people))
                    if sorted_tmp_people in visited: tmp_people[p] = [k, a, b]; continue
                    stair_people.append([arr[k][a][b], 0])
                    tmp_people.pop(p)
                    visited.add(sorted_tmp_people)
                    arr[arr[k][a][b]][1] += 1

    break
