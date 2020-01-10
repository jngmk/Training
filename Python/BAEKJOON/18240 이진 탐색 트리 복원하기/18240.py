import sys
sys.setrecursionlimit(1000000)


def find_depth(num):
    idx = 1
    cnt = 0
    while True:
        if not tree.get(idx):
            return cnt, idx
        if num > tree[idx]:
            idx = idx * 2 + 1
        else:
            idx = idx * 2
        cnt += 1


def permutation(k, seq):
    global sequence, find, tree
    if k == N:
        find = True;
        sequence = ' '.join(map(str, seq))
        return
    else:
        for i in range(1, N+1):
            if visited[i]: continue
            cnt, idx = find_depth(i)
            if cnt != arr[k-1]: continue
            tree[idx] = i
            visited[i] = 1
            permutation(k+1, seq + [i])
            tree.pop(idx)
            visited[i] = 0


N = int(input())
arr = list(map(int, input().strip().split()))
depth = max(arr)
# 한쪽으로 쏠렸을 때를 생각해서 처음 시작 범위를 줄인다.
tree = dict()
find = False
sequence = ''
visited = [0] * (N+1)
for head in range(1, N):
    tree[1] = head
    visited[head] = 1
    permutation(1, [head])
    visited[head] = 0
    if find: break
    tree.pop(1)

print(sequence if find else -1)
