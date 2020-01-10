from collections import deque

N, a, b = map(int, input().split())
meet = False
min_d = 0
value = abs(a-b)
selected = []
if value % 2 == 0:
    moves = [0, 1]
    num = 1
    day = 1
    while True:
        num *= 2
        if num > N//2: break
        moves.append(num)
        day += 1
    # print(moves)
    value //= 2
    for i in range(day, 0, -1):
        # 만날 수 있는 상태인지 확인
        if value >= moves[i]:
            value -= moves[i]
            selected.append(i)
        if value == 0:
            break
    # print(selected, value)

    if value == 0:
        # min_d = day+1
        s = len(selected) - 1
        q = deque([(a, b, 1, s)])  # 위치, 날짜
        while q:
            # print(q)
            if meet: break
            a, b, d, s = q.popleft()
            dd = moves[d]
            move = [(a-dd, b-dd), (a+dd, b+dd)]
            # print(d, selected[s])
            if d == selected[s]:
                s -= 1
                move = [(a+dd, b-dd), (a-dd, b+dd)]

            for na, nb in move:
                if not (1 <= na <= N and 1 <= nb <= N): continue
                # print(d+1, day)
                if d > day: continue
                if s == -1: meet = True; break

                q.append((na, nb, d+1, s))

print(selected[0] if meet else -1)
