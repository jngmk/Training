from collections import deque
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M, K, idx1, idx2 = map(int, input().split())
    D1, D2 = list(map(int, input().split())), list(map(int, input().split()))
    desk1, desk2 = [[0, 0]] * N, [[0, 0]] * M
    tmp1, tmp2 = deque(), deque()
    people = list(map(int, input().split()))
    visited = [0] * (K+1)
    completed = 0
    result = 0

    while completed != K:
        # 업무보기
        # 정비
        for d2 in range(M):
            p, t = desk2[d2][0], desk2[d2][1]
            if p: t += 1; desk2[d2][1] = t
            if t == D2[d2]:
                if d2 == idx2-1: visited[p] += 1
                desk2[d2] = [0, 0]
                completed += 1
            if visited[p] == 2: result += p

        # 접수
        for d1 in range(N):
            p, t = desk1[d1][0], desk1[d1][1]
            if p: t += 1; desk1[d1][1] = t
            if t == D1[d1]:
                if d1 == idx1-1: visited[p] += 1
                tmp2.append(p)
                desk1[d1] = [0, 0]

        # 사람
        for p in range(K):
            if people[p] < 0: continue
            if people[p] == 0:
                tmp1.append(p+1)
                # print(tmp1)
            people[p] -= 1

        # 빈 곳에 들어가기
        # 정비
        for d2 in range(M):
            p, t = desk2[d2][0], desk2[d2][1]
            if not p and tmp2:
                desk2[d2] = [tmp2.popleft(), 1]

        # 접수
        for d1 in range(N):
            p, t = desk1[d1][0], desk1[d1][1]
            if not p and tmp1:
                desk1[d1] = [tmp1.popleft(), 1]
        # print(desk1, desk2)
    print('#{} {}'.format(tc, result))
    # break
