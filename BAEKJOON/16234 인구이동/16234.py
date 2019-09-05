N, L, R = map(int, input().split())
array = [list(map(int, input().split())) + [1000] for _ in range(N)]
array += [[1000] * (N+1)]
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
stack = [0] * N * N
top = -1


def is_range(num1, num2):
    if L <= abs(num1-num2) <= R:
        return True
    else:
        return False


immigration = 0
while True:
    is_visited = [[0] * (N+1) for _ in range(N+1)]
    v1, v2 = -1, -1
    for a in range(N):
        for b in range(N):
            people = 0
            if (is_range(array[a][b], array[a][b+1]) or is_range(array[a][b], array[a+1][b])) and not is_visited[a][b]:
                if not is_visited[a+1][b] and not is_visited[a][b+1]:
                    stack[top+1] = (a, b)
                    top += 1
                    is_visited[a][b] = 1
                    people += array[a][b]
                    union = [(a, b)]
                    while top != -1:
                        v1, v2 = stack[top]
                        top -= 1
                        for d in range(4):
                            rv1 = v1 + da[d]
                            rv2 = v2 + db[d]
                            if 0 <= rv1 < N and 0 <= rv2 < N:
                                if is_range(array[v1][v2], array[rv1][rv2]) and not is_visited[rv1][rv2]:
                                    stack[top+1] = rv1, rv2
                                    top += 1
                                    is_visited[rv1][rv2] = 1
                                    people += array[rv1][rv2]
                                    union.append((rv1, rv2))

                    new_people = people // len(union)
                    while union:
                        u1, u2 = union.pop()
                        array[u1][u2] = new_people

    if v1 < 0:
        break
    immigration += 1

print(immigration)
