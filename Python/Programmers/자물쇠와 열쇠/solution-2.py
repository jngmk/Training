def solution(key, lock):
    N, M = len(lock), len(key)
    key2 = [[key[a][b] for a in range(M-1, -1, -1)] for b in range(M)]
    key3 = [[key[a][b] for a in range(M)] for b in range(M-1, -1, -1)]
    key4 = [[key[a][b] for a in range(M-1, -1, -1)] for b in range(M-1, -1, -1)]
    # 빈 공간
    vacant = []
    for a in range(N):
        for b in range(N):
            if lock[a][b] == 0:
                vacant.append((a, b))
    print(vacant)

    for k in [key, key2, key3, key4]:
        keys = []
        for a in range(M):
            for b in range(M):
                if k[a][b] == 1:
                    keys.append((a, b))
        print(k)
        print(keys)
        # key_idx = [0] * (len(key))
        for a in range(M):
            for b in range(M):
                if k[a][b] == 1:
                    print('a, b', a, b)
                    d1, d2 = vacant[0][0]-a, vacant[0][1]-b
                    print('d1, d2', d1, d2)
                    for v1, v2 in vacant:
                        m1, m2 = v1-d1, v2-d2
                        print('m1, m2', m1, m2)
                        if not (0 <= m1 < M and 0 <= m2 < M): break
                        if k[m1][m2] == 0:
                            break
                    else:
                        # return True
                        for k1, k2 in keys:
                            n1, n2 = k1+d1, k2+d2
                            print('d1, d2', d1, d2)
                            print('n1, n2', n1, n2)
                            if not (0 <= n1 < N and 0 <= n2 < N): break
                            if lock[n1][n2] == 1: break
                        else:
                            return True

    return False


print(solution([[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1]]))
