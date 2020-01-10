from collections import deque

N, a, b = map(int, input().split())
meet = False
min_d = 0
if abs(a - b) % 2 == 0:
    moves = [0, 1]
    num = 1
    day = 1
    while True:
        num *= 2
        if num > N//2: break
        moves.append(num)
        day += 1
    print(moves)
    status = 0
    for i in range(1, day+1):
        # 만날 수 있는 상태인지 확인
        if abs(a - b) == moves[i] * 2:
            status = 1
            break

    q = deque([(a, b, 1, status)])
    min_d = day+1
    if status == 0:
        while q:
            a, b, d, s = q.popleft()

            if abs(a - b) == moves[d] * 2:
                meet = True; min_d = d
                break

            dd = moves[d]
            move = [[(a+dd, b+dd), (a+dd, b-dd), (a-dd, b+dd), (a-dd, b-dd)],
                   [(a-dd, b-dd), (a+dd, b+dd)]]
            for na, nb in move[s]:

                if not (1 <= na <= N and 1 <= nb <= N): continue
                if d + 1 > day: continue
                # 움직이는 거리가 두 오리 사이의 거리보다 커져서 못 만나는 경우
                if abs(na - nb) < moves[d+1] * 2: continue

                ss = s
                # 만날 수 있는 상태인지 확인
                if s == 0:
                    for ddd in range(d+1, day+1):
                        if abs(na - nb) == moves[ddd] * 2: ss = 1; break
                q.append((na, nb, d+1, ss))

print(min_d if meet else -1)
