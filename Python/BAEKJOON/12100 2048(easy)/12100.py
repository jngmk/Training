def solve(d):
    if d == 0:
        pass
    elif d == 1:
        pass
    elif d == 2:
        pass
    else:
        pass
    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
tmp_arr = []
q = []

for _ in range(5):
    tmp_arr = [[arr[a][b] for b in range(N)] for a in range(N)]
    for dd in range(4):
        solve(dd)
