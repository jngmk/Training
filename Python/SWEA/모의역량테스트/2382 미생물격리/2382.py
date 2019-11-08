import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
convert = {1: 2, 2: 1, 3: 4, 4: 3}
vanish = []


def move(aa, bb, nn, dd):
    da, db = direction[dd]
    aa = aa + da
    bb = bb + db

    if aa == 0 or aa == N-1 or bb == 0 or bb == N-1:
        nn //= 2
        dd = convert[dd]

    return [aa, bb, nn, dd]


for i in range(1, T+1):
    N, M, K = map(int, input().split())
    bacteria = [0] * K
    for k in range(K):
        a, b, num, d = list(map(int, input().split()))
        bacteria[k] = [a, b, num, d]

    for _ in range(M):
        for n in range(len(bacteria)):
            a, b, num, d = bacteria[n]
            bacteria[n] = move(a, b, num, d)
            if bacteria[n][2] == 0:
                vanish.append(n)

        meet = {}
        for n in range(len(bacteria)):
            a, b, num, d = bacteria[n]
            if meet.get(a*1000+b):
                meet.get(a*1000+b).append([num, n])
            else:
                meet.update({a*1000+b: [[num, n]]})
        meet = sorted(meet.values())

        for m in range(len(meet)):
            if len(meet[m]) > 1:
                meet[m] = sorted(meet[m])
                for mm in meet[m][:-1]:
                    idx = meet[m][-1][1]
                    bacteria[idx][2] += mm[0]
                    vanish.append(mm[1])

        vanish = sorted(vanish)
        while vanish:
            idx = vanish.pop()
            bacteria.pop(idx)

    result = 0
    for n in range(len(bacteria)):
        result += bacteria[n][2]

    print('#{} {}'.format(i, result))
