def comb(k, now, temp):
    global result
    if k == N//2:
        group1 = temp
        group2 = [x for x in range(1, N+1) if x not in temp]
        pop1 = pop2 = 0
        if len(group1) != 0:
            if dfs(group1) and dfs(group2):
                for p in range(1, N+1):
                    if p in group1:
                        pop1 += populations[p]
                    else:
                        pop2 += populations[p]
                temp_res = abs(pop1 - pop2)
                result = min(result, temp_res)
        return
    else:
        for i in range(now+1, N+1):
            comb(k+1, i, temp)
            comb(k+1, i, temp+[i])


def dfs(group):
    temp_visited = [0] * (N+1)
    stack = [group[0]]
    while stack:
        v = stack.pop()
        temp_visited[v] = 1
        for w in range(1, arr[v][0]+1):
            if not temp_visited[arr[v][w]] and arr[v][w] in group:
                stack.append(arr[v][w])
                temp_visited[arr[v][w]] = 1
    if len(group) == sum(temp_visited):
        return True


N = int(input())
populations = [0] + list(map(int, input().split()))
arr = [[0]] + [list(map(int, input().split())) for _ in range(N)]
result = 100000000
comb(0, 0, [])

if result == 100000000:
    result = -1
print(result)
