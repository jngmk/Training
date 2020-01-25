# 돌기 문제 해결 필요

def solution(key, lock):
    N, M = len(lock), len(key)
    key2 = [[key[a][b] for a in range(M-1, -1, -1)] for b in range(M)]
    key3 = [[key[a][b] for a in range(M)] for b in range(M-1, -1, -1)]
    key4 = [[key[a][b] for a in range(M-1, -1, -1)] for b in range(M-1, -1, -1)]
    # 자물쇠 빈 공간
    vacant = []
    vcnt = 0
    for a in range(N):
        for b in range(N):
            if lock[a][b] == 0:
                vacant.append((a, b))
                vcnt += 1
    print(vcnt, vacant)

    for k in [key, key2, key3, key4]:
        print(k)
        for da in range(N):
            for db in range(N):
                cnt = 0
                possible = True
                for a in range(M):
                    for b in range(M):
                        m1, m2 = a+da, b+db
                        print('a, b, m1, m2', a, b, m1, m2)
                        if not (0 <= m1 < N and 0 <= m2 < N): continue
                        if k[m1][m2] == lock[m1][m2]: possible = False; break
                        elif k[m1][m2] == 1 and lock[m1][m2] == 0: cnt += 1
                    if not possible: break
                else:
                    if cnt == vcnt: return True

    return False


print(solution([[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1]]))
