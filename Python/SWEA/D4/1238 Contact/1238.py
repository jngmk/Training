import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    L, S = map(int, input().split())
    num_list = list(map(int, input().split()))
    array = [[0] * 101 for _ in range(101)]
    for i in range(L // 2):
        a = num_list[2 * i]
        b = num_list[2 * i + 1]
        array[a][b] = 1

    queue = [0] * L * L
    front = -1
    rear = -1
    is_visited = [0] * 101
    length = 0

    queue[front+1] = (S, length)
    front += 1
    is_visited[S] = 1

    while front != rear:
        v, length = queue[rear+1]
        rear += 1
        for y in range(101):
            if array[v][y] == 1 and not is_visited[y]:
                queue[front+1] = (y, length + 1)
                front += 1
                is_visited[y] = 1

    max_l = 0
    max_num = 0
    for num, l in reversed(queue[:front+1]):
        if l >= max_l:
            max_l = l
            if num > max_num:
                max_num = num
        else:
            break

    print('#{0} {1}'.format(t, max_num))


'''
def BFS(v):
    ans = f = r = -1
    visited = [0] * 101
 
    r += 1; q[r] = v
    visited[v] = 1;
    r += 1; q[r] = -1       # 같은 레벨 마크
 
    while True:
        f += 1; v = q[f]
        if ans < v : ans = v
 
        if v == -1:
            if f == r : return ans
            r += 1; ans = q[r] = -1
            continue
 
        for i in range(G[v][0]):
            if not visited[G[v][i + 1]]:
                visited[G[v][i + 1]] = 1
                r += 1; q[r] = G[v][i + 1]
 
q = [0] * 200
for tc in range(1, 11):
    N, S = map(int, input().split())
    G = [[0] * 100 for i in range(101)]
    edges = list(map(int, input().split()))
 
    for i in range(N//2):
        u, v = edges[i*2: i*2 + 2]
        G[u][0] += 1
        G[u][G[u][0]] = v
 
    print('#%d'%tc, BFS(S))
'''