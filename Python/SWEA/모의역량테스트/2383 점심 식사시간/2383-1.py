import sys
sys.stdin = open('input.txt')


def comb(k, now, temp):
    global group1, group2
    if k == len(people):
        temp1 = [i for i in range(len(people)) if i not in temp]
        group1.append(temp)
        group2.append(temp1)
    else:
        for j in range(now, len(people)):
            comb(k+1, j+1, temp)
            comb(k+1, j+1, temp+[j])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people, stairs = [], []
    s_length = []
    group1, group2 = [], []
    result = float('inf')
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 1:
                people.append([a, b])
            elif arr[a][b] > 1:
                stairs.append([a, b])
                s_length.append(arr[a][b])
    comb(0, 0, [])

    for g in range(len(group1)):
        times1, times2, stair1, stair2 = [], [], [], []
        # 그룹1
        minutes1 = 0
        a, b = stairs[0]
        for g1 in group1[g]:
            c, d = people[g1]
            times1.append(abs(a-c)+abs(b-d))
        # 그룹1 - 계단1 시간
        while times1 or stair1:
            # 계단 올라가기
            for s in range(len(stair1)-1, -1, -1):
                stair1[s] += 1
                if stair1[s] == s_length[0]:
                    stair1.pop(s)
            # 계단으로 움직이기
            for t in range(len(times1)-1, -1, -1):
                if times1[t] == 0:
                    if len(stair1) != 3:
                        times1.pop(t)
                        stair1.append(0)
                    else:
                        continue
                else:
                    times1[t] -= 1
            minutes1 += 1
        if minutes1 > result: continue

        # 그룹2
        minutes2 = 0
        a, b = stairs[1]
        for g2 in group2[g]:
            c, d = people[g2]
            times2.append(abs(a-c)+abs(b-d))

        # 그룹2 - 계단2 시간
        while times2 or stair2:
            # 계단 올라가기
            for s in range(len(stair2)-1, -1, -1):
                stair2[s] += 1
                if stair2[s] == s_length[1]:
                    stair2.pop(s)
            # 계단으로 움직이기
            for t in range(len(times2)-1, -1, -1):
                if times2[t] == 0:
                    if len(stair2) != 3:
                        times2.pop(t)
                        stair2.append(0)
                    else:
                        continue
                else:
                    times2[t] -= 1
            minutes2 += 1
        result = min(result, max(minutes1, minutes2))
        if minutes2 > result: continue
    print('#{} {}'.format(tc, result))
