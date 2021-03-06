# 속도 좀 더 빠른 버전
T = int(input())
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
for i in range(1, T + 1):
    N, K = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    peak = []
    max_h = 0
    for a in range(N):
        for b in range(N):
            if max_h < array[a][b]:
                peak = [(a, b)]
                max_h = array[a][b]
            elif max_h == array[a][b]:
                peak.append((a, b))
    stack = [0] * N * N
    top = -1
    max_l = 0
    for a, b in peak:
        is_visited = [(a, b)]
        stack[top + 1] = a, b, 1, max_h, 1, is_visited
        top += 1
        while top != -1:
            v1, v2, length, val, chk, is_visited = stack[top]  # 좌표, 등산로길이, 현재높이, 공사실행여부, 지나온길
            top -= 1
            for d in range(4):
                va = v1 + da[d]
                vb = v2 + db[d]
                if 0 <= va < N and 0 <= vb < N:
                    if array[va][vb] < val + K and (va, vb) not in is_visited:  # 공사능력 범위 안이라면
                        if array[va][vb] >= val:
                            if chk == 1:
                                for k in range(1, K + 1):
                                    if array[va][vb] - k < val:
                                        stack[top + 1] = va, vb, length + 1, array[va][vb] - k, 0, is_visited + [
                                            (va, vb)]
                                        top += 1
                        else:
                            if array[va][vb] < val:
                                stack[top + 1] = va, vb, length + 1, array[va][vb], chk, is_visited + [(va, vb)]
                                top += 1

            if max_l < length:
                max_l = length

    print('#{} {}'.format(i, max_l))
