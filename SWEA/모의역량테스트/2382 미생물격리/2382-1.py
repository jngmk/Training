import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
da = [0, -1, 1, 0, 0]
db = [0, 0, 0, -1, 1]
vanish = []
for i in range(1, T+1):
    N, M, K = map(int, input().split())
    bacteria = [0] * K
    for k in range(K):
        a, b, num, d = list(map(int, input().split()))
        bacteria[k] = [a, b, num, d]

    for _ in range(M):
        for n in range(len(bacteria)):
            a, b, num, d = bacteria[n]
            bacteria[n][0], bacteria[n][1] = a + da[d], b + db[d]
            if a + da[d] == 0 or a + da[d] == N-1 or b + db[d] == 0 or b + db[d] == N-1:
                if d == 2 or d == 4:
                    d -= 1
                else:
                    d += 1
                num //= 2
                if num == 0:
                    vanish.append(n)
            bacteria[n][2], bacteria[n][3] = num, d

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
