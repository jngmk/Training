from collections import deque

road = [0, 0, 0, 0]
road[0] = list(range(0, 42, 2)) + [41]
road[1] = [10, 13, 116, 19, 25, 130, 35, 40, 41]
road[2] = [20, 222, 224, 25, 130, 35, 40, 41]
road[3] = [30, 328, 27, 326, 25, 130, 35, 40, 41]
visited = set()
dices = list(map(int, input().split()))
result = 0
q = deque()
tmp_q = deque()
q.append([[[0, 0], [0, 0], [0, 0], [0, 0]], 0])

for d in dices:
    while q:
        horses, total = q.popleft()
        for i in range(4):
            h = [horses[0], horses[1], horses[2], horses[3]]
            p = [road[h[0][0]][h[0][1]], road[h[1][0]][h[1][1]], road[h[2][0]][h[2][1]], road[h[3][0]][h[3][1]]]
            # 도착하면 움직이지 않음
            if p[i] == 41:
                continue
            # 하나씩 움직여서 저장해봄
            a, b = h[i][0], h[i][1]
            b += d
            # 도착점을 넘을 경우 도착점에 저장
            if b >= len(road[a]):
                b = len(road[a]) - 1
            # 파란 원에 멈출 때 경로 변경
            if a == 0 and road[a][b] == 10:
                a, b = 1, 0
            elif a == 0 and road[a][b] == 20:
                a, b = 2, 0
            elif a == 0 and road[a][b] == 30:
                a, b = 3, 0
            pos = road[a][b]
            if pos != 0 and pos != 41 and pos in p:
                continue
            p[i] = pos
            pos %= 100
            if pos == 41:
                pos = 0
            p = list(sorted(p))
            # 해당 조합의 경우를 확인하지 않았다면
            if (p[0], p[1], p[2], p[3], total+pos) not in visited:
                visited.add((p[0], p[1], p[2], p[3], total+pos))
                h[i] = [a, b]
                tmp_q.append([h, total+pos])
                result = max(result, total+pos)
    q = tmp_q
    tmp_q = deque()

print(result)
