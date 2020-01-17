def solution(key, lock):
    N, M = len(lock), len(key)
    key2 = [[key[a][b] for a in range(M-1, -1, -1)] for b in range(M)]
    key3 = [[key[a][b] for a in range(M)] for b in range(M-1, -1, -1)]
    key4 = [[key[a][b] for a in range(M-1, -1, -1)] for b in range(M-1, -1, -1)]

    # 빈 공간
    vacant = dict()
    total = 0
    for a in range(N):
        for b in range(N):
            if lock[a][b] == 0:
                vacant[(a, b)] = 1
                total += 1
    print(vacant)

    for k in [key, key2, key3, key4]:
        print(k)
        for d in range(N):
            print('d', d)
            visited = 0
            possible = True
            for a in range(M):
                for b in range(M):
                    if k[a][b] == 1:
                        n1, n2 = a+d, b+d
                        if 0 <= n1 < N and 0 <= n2 < N:
                            print(n1, n2, lock[n1][n2])
                            # 자물쇠가 0 이면 괜찮음
                            if lock[n1][n2] == 1: possible = False; break
                            visited += 1
                if not possible: break
            else:
                print('visited', visited)
                if visited == total:
                    return True

    return False


print(solution([[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1]]))
